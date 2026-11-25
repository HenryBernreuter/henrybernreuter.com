---
date: 2026-11-25 00:00:00
layout: post
title: "Build a Company Knowledge Base in Microsoft Teams with a Copilot Agent"
subtitle: "Right now, your company's knowledge base is you. Here's the full technical build: admin setup, SharePoint structure, the agent, permission testing, and the automations that keep it honest."
description: A detailed technical walkthrough for building a permission-aware company knowledge base in Microsoft Teams and SharePoint with a Microsoft 365 Copilot Agent Builder agent, PowerShell setup scripts, and Power Automate flows.
image: /assets/img/teams-knowledge-base-hero.png
optimized_image: /assets/img/teams-knowledge-base-hero.png
category: tutorial
tags:
  - microsoft-teams
  - copilot
  - sharepoint
  - microsoft-365
  - power-automate
  - powershell
  - ai-agents
toc: true
author: henry
---

It's 6:40 on a Tuesday evening, and the owner of a fifteen-person heating and air company is at his kid's soccer game. His phone buzzes. A technician wants to know the after-hours fee. Then the office manager asks where the current price list is. Then a dispatcher asks whether she can approve a $200 refund on her own.

Every answer exists somewhere: a Word file, an old email, a PDF on someone's desktop. But the fastest way to find any of it is to text the owner. The company has a knowledge base, and it's him.

This post builds the real one, end to end, on Microsoft 365: **Teams** holds the documents, **SharePoint** stores them and enforces permissions, a **Copilot agent** answers questions from them, and **Power Automate** keeps the whole thing from going stale. I'll cover the clicks, the PowerShell to script the setup, the admin settings people forget, and the places it breaks.

---

## How It Works: A Library with Library Cards

One picture holds the whole design together:

- **Documents are the books.** One topic per file.
- **Teams is the building; each channel is a shelf.** Under the hood, a team is a SharePoint site and each standard channel is a folder in that site's document library.
- **The Copilot agent is the librarian.** It doesn't memorize anything. For each question, it searches the SharePoint content you pointed it at, retrieves the relevant passages, and answers with a link to the source. That's retrieval-augmented generation, the same pattern I built by hand in [Build a RAG Chatbot on Databricks](/databricks-build-a-rag-chatbot/).
- **Everyone has a library card.** The agent searches **as the person asking**. Microsoft's documentation is explicit: the agent "respects existing permissions and sensitivity labels for files already uploaded to SharePoint or OneDrive." If you can't open a file, the agent can't use it to answer you.

That last property is what makes this safe to deploy, and Step 5 is about proving it holds.

---

## Step 0: Admin Prerequisites (Do These First)

Most failed builds trace back to something in this section. You'll need a Microsoft 365 admin for parts of it.

### 0.1 Decide how people will be licensed

Answering from SharePoint content is a paid capability. Microsoft's prerequisites page draws the line clearly: Copilot Chat users **without** usage-based billing can't ground agents in SharePoint data. Each person who asks the agent questions needs **one** of these:

**Option A: a Microsoft 365 Copilot license** (Copilot for enterprise at $30/user/month, or Microsoft 365 Copilot Business for smaller organizations; check [current pricing](https://www.microsoft.com/en-us/microsoft-365/copilot/business), which has had promotions in 2026). Assign it in the **Microsoft 365 admin center → Users → Active users → select the user → Licenses and apps**.

**Option B: pay-as-you-go** for unlicensed users, metered in **Copilot Credits** and billed to an Azure subscription. Setup, per Microsoft's documentation:

1. You need the **Billing Administrator**, **AI Administrator**, or **Global Administrator** role, plus **Owner** or **Contributor** on an Azure subscription in the **same tenant** as Microsoft 365.
2. In the Microsoft 365 admin center, go to **Copilot → Billing & usage → Billing policies → Add a billing policy**.
3. Pick the Azure subscription and resource group (or create new ones in the wizard), then **add the users or security group** the policy covers. Use a security group, like `sg-handbook-users`, so access is managed in one place.
4. Optionally set a budget. Note that Microsoft says the budget is for alerting: "the system doesn't enforce the budget or prevent your organization from exceeding it."
5. Go to the **Pay-as-you-go services** tab and connect the **SharePoint agents** service (and **Microsoft Copilot Chat**, if you want it) to the policy.

Only users in the policy's security group get the SharePoint-grounded experience. If you later turn pay-as-you-go off, Microsoft notes it can take up to two hours for users to lose access.

A common mix for a small business: Copilot licenses for the few people who use Copilot all day, and pay-as-you-go for everyone else.

### 0.2 Make sure agents are allowed

In the Microsoft 365 admin center, open **Agents → Settings**:

- **User access**: who can use agents (default: all users).
- **Sharing**: who can share Agent Builder agents org-wide (default: all users). Setting this to "No users" still allows sharing with specific people.
- **Agent and plugin access**: make sure agents **built by your organization** are allowed, or yours won't show up for anyone.

### 0.3 Check that SharePoint search isn't restricted

If your tenant has **Restricted SharePoint Search** enabled, Agent Builder can't use SharePoint as a knowledge source at all. Microsoft is retiring that feature (new enablement has been blocked since July 31, 2026), but older tenants may still have it on. Check from PowerShell:

```powershell
Install-Module Microsoft.Online.SharePoint.PowerShell -Scope CurrentUser
Connect-SPOService -Url https://contoso-admin.sharepoint.com

Get-SPOTenantRestrictedSearchMode     # should return Disabled
```

If it returns `Enabled`, talk to whoever turned it on before going further. Its replacement, **Restricted Content Discovery**, is applied per site. If your admin uses it, confirm it isn't applied to the handbook sites.

Throughout this post, replace `contoso` with your tenant name.

---

## Step 1: Build the Shelves (Team, Channels, Sites)

### In the Teams client

1. **Teams → New items → New team → From scratch → Private**. Name it **Company Handbook**.
2. Add members. Everyone who should read the general handbook goes in as a **Member**. Two or three people who maintain it go in as **Owners**.
3. Add **standard channels**, one per department: Sales, Field Operations, Dispatch, Office.
4. Add a **private channel** named **HR**, and add only the people allowed to see HR material.

### Or script it

The `MicrosoftTeams` module does the same thing repeatably, which is handy if you ever rebuild:

```powershell
Install-Module MicrosoftTeams -Scope CurrentUser
Connect-MicrosoftTeams

$team = New-Team -DisplayName "Company Handbook" -Visibility Private `
                 -Description "Policies, prices, and procedures"

foreach ($name in "Sales", "Field Operations", "Dispatch", "Office") {
    New-TeamChannel -GroupId $team.GroupId -DisplayName $name
}

# Private channel: gets its own SharePoint site with its own membership
New-TeamChannel -GroupId $team.GroupId -DisplayName "HR" `
                -MembershipType Private -Owner "maria@contoso.com"

Add-TeamUser -GroupId $team.GroupId -User "tech1@contoso.com" -Role Member
Add-TeamChannelUser -GroupId $team.GroupId -DisplayName "HR" -User "hr1@contoso.com"
```

### Understand what you just created

This is the part that matters for the agent:

| Teams object | SharePoint reality | Who can read it |
|---|---|---|
| The team | A SharePoint site, e.g. `https://contoso.sharepoint.com/sites/CompanyHandbook` | Team members |
| A standard channel | A **folder** in that site's **Documents** library | Team members |
| A private channel | Its **own separate site** | Only that channel's members |

Microsoft's documentation confirms that "each private channel has its own SharePoint site," and that people in the parent team, and even admins, don't get access unless they're channel members. That's your locked HR room.

You'll need both site URLs in Step 3. The reliable way to get them: open the channel in Teams, go to the **Files** tab, choose **Open in SharePoint**, and copy the address up to and including the site name (`https://contoso.sharepoint.com/sites/<SiteName>`). Or list the private channel sites from PowerShell, since they use the `TEAMCHANNEL` site template:

```powershell
Get-SPOSite -Limit All |
    Where-Object { $_.Template -like "TEAMCHANNEL*" } |
    Select-Object Title, Url
```

---

## Step 2: Prepare the Libraries and the Books

### 2.1 Add metadata columns

Each document gets an **owner** and a **last reviewed** date. Power Automate uses both in Step 7.

Create the columns with clean internal names. SharePoint fixes a column's internal name when the column is created, so a column created as "Last reviewed" gets the internal name `Last_x0020_reviewed`, and you'll be typing that in filter queries forever. Create it as `LastReviewed`, then rename the display name. PnP PowerShell lets you set both directly:

```powershell
Install-Module PnP.PowerShell -Scope CurrentUser    # PnP 3.x needs PowerShell 7.4+

# One-time: PnP needs its own Entra app registration for interactive sign-in
Register-PnPEntraIDAppForInteractiveLogin -ApplicationName "PnP Handbook Admin" `
    -Tenant contoso.onmicrosoft.com -Interactive

$sites = "https://contoso.sharepoint.com/sites/CompanyHandbook",
         "https://contoso.sharepoint.com/sites/CompanyHandbook-HR"   # use your HR site URL from Step 1

foreach ($site in $sites) {
    Connect-PnPOnline -Url $site -Interactive -ClientId "<app-id-from-registration>"
    Add-PnPField -List "Documents" -DisplayName "Last reviewed" -InternalName "LastReviewed" `
                 -Type DateTime -AddToDefaultView
    Add-PnPField -List "Documents" -DisplayName "Doc owner" -InternalName "DocOwner" `
                 -Type User -AddToDefaultView
}
```

(I use `DocOwner` rather than `Owner`, because "Owner" is ambiguous next to SharePoint's own ownership concepts.)

### 2.2 Write documents the retriever can find

The agent finds passages by searching. The way you write a document decides whether the right passage comes back.

**One topic per file, named the way people ask.** `After-Hours and Weekend Fees.docx`, not `Policy_v3_FINAL.docx`. Avoid `&` in file names and paths; Microsoft's troubleshooting guidance lists ampersands among the causes of retrieval failures.

**Put the answer in the first lines.** Start every document with a fixed header block:

```
After-Hours and Weekend Fees
Summary: Calls between 6 PM and 7 AM, and on weekends, add a $150 fee.
         Holidays add $225. Dispatch can waive the fee for warranty callbacks.
Owner: Maria Lopez (Office Manager)
Last reviewed: November 2026
```

The summary gives the retriever a dense, quotable chunk. "Owner" and "Last reviewed" in the body help human readers. The matching SharePoint columns drive the automation.

**Use headings and bullets, not tables.** Microsoft's content-retrieval guidance says "Copilot is currently unable to parse tables and other special formatting in SharePoint content." Convert price tables into lists:

```
## Residential service rates
- Diagnostic visit: $89
- After-hours fee (6 PM to 7 AM): $150
- Holiday fee: $225
```

**Keep files short.** Microsoft recommends keeping SharePoint files to "a maximum of 36,000 characters (approximately 15-20 pages)." Split long handbooks by topic.

**Make every file real text.** A scanned PDF is an image with no text layer, so the retriever sees nothing. Open it in Word (which converts PDFs on open), check the result carefully, and save it as `.docx`.

**Remove duplicates and old versions.** If two documents give different after-hours fees, the agent may quote either one. Keep one authoritative file per topic. SharePoint's built-in version history already keeps the old versions.

**Mind the limits.** An Agent Builder agent can use up to **100 SharePoint files**, and you can point it at one SharePoint list. A focused small-business handbook fits easily. A dump of every file the company has ever made does not.

### 2.3 Upload and tag

Upload each document in its channel's **Files** tab, then fill in **Doc owner** and **Last reviewed** in SharePoint's library view. To audit what you have, list every file with its size and review date:

```powershell
Connect-PnPOnline -Url "https://contoso.sharepoint.com/sites/CompanyHandbook" -Interactive -ClientId "<app-id>"

Get-PnPListItem -List "Documents" -PageSize 500 |
    Where-Object { $_.FileSystemObjectType -eq "File" } |
    ForEach-Object {
        [pscustomobject]@{
            File         = $_["FileLeafRef"]
            Path         = $_["FileRef"]
            SizeKB       = [math]::Round($_["File_x0020_Size"] / 1KB)
            LastReviewed = $_["LastReviewed"]
            Owner        = $_["DocOwner"].Email
        }
    } | Sort-Object LastReviewed | Format-Table -AutoSize
```

Files with an empty `LastReviewed` or `Owner` are your to-do list before launch.

---

## Step 3: Configure the Agent

Agent Builder runs in the Microsoft 365 Copilot app (at microsoft365.com/chat) and in the Teams desktop and web clients. It doesn't run on mobile. Choose **New agent** in the left pane. You'll get two tabs: **Describe** (build by conversation) and **Configure** (set fields directly). Use **Configure**, so every setting is deliberate.

### 3.1 Name and description

- **Name:** Company Handbook Assistant
- **Description:** Answers employee questions about company policies, prices, and procedures, with links to the source document.

### 3.2 Instructions

The instructions are your main control over behavior. Write them like a spec:

```
Role: You answer employee questions for Contoso Heating & Air using ONLY the
Company Handbook documents in your knowledge sources.

Rules:
1. Every answer must cite and link the document it came from. If you cannot
   cite a handbook document, you do not have an answer.
2. If the handbook does not cover the question, reply exactly:
   "The handbook doesn't cover that yet. Ask a human here: <Forms link>"
   Do not guess. Do not use general knowledge to fill gaps.
3. Prices, fees, pay, legal, and safety: quote the document's exact wording
   and numbers. Never round or estimate.
4. If two documents conflict, show both, cite both, and tell the user to
   confirm with the owners named in the documents.
5. Format: answer first in one or two sentences, then "Source:" with the link.
   Keep answers under 120 words unless the user asks for detail.
```

### 3.3 Knowledge

Under **Knowledge**, choose **Enter URL** and paste the main site:

```
https://contoso.sharepoint.com/sites/CompanyHandbook
```

Press Enter. Then add the HR private channel's site the same way. It's a separate site, so the main site URL doesn't cover it. Microsoft's rules for the URL: include the site path, and **no query parameters** (nothing after a `?`). If you copied a link with `?web=1` or similar on the end, trim it.

If you keep structured data in a SharePoint list (a parts catalog, for example), add it by its own list URL. A site URL doesn't pull in the site's lists, and filtered list views can't be used.

### 3.4 Scope settings

- **Search all websites: off.** A handbook assistant shouldn't answer from the public internet.
- **Only use specified sources: on.** Here's the caveat most tutorials miss. Microsoft documents that this setting makes the agent *prioritize* your sources, and that it "doesn't support blocking general AI knowledge from your agent's responses." Search-type questions go to your files. If nothing is found, the agent gives a can't-find response. Simple questions ("what's 15% of $340?") may still be answered from general knowledge. Rule 2 in your instructions is the second layer of defense. If you need a hard guarantee, that's a Copilot Studio feature (see the end of this post).

### 3.5 Starter prompts

Add three to five real questions people can click: "What's the after-hours fee?", "What's our refund approval limit?", "Who do I call for a warranty part?". They teach people what the agent is for.

### 3.6 Never upload sensitive files into the agent

The Knowledge section also lets you **upload** files directly into the agent. For anything sensitive, don't. Microsoft is explicit: for uploaded files, "any user who has access to the agent also has access to the information in the file." Uploaded files bypass SharePoint permissions entirely. Uploads are fine for genuinely public material. Everything else stays in SharePoint.

Then select **Create**. When you edit the agent later, changes aren't visible to users until you select **Update**.

---

## Step 4: Test Answer Quality

Use the **Try it** pane before anyone else sees the agent. Build a small test set from the questions people actually ask, and record the expected answer and source for each:

| # | Question | Expected answer | Expected source |
|---|---|---|---|
| 1 | What's the after-hours fee? | $150, 6 PM to 7 AM | After-Hours and Weekend Fees |
| 2 | Can dispatch waive the after-hours fee? | Yes, for warranty callbacks | After-Hours and Weekend Fees |
| 3 | What's our refund approval limit? | $250 without manager approval | Refunds and Credits |
| 4 | What's the company's stock price? | "The handbook doesn't cover that yet..." | none |

Row 4 is the most important. A good knowledge agent says "I don't know" confidently. If it invents an answer, tighten the instructions and retest.

For every wrong answer, debug in this order:

1. **Retrieval.** Did it cite the right document? If not, the document's title or summary probably doesn't match how people phrase the question. Rewrite the summary line using their words.
2. **Content.** Is the right answer actually in the document, in text rather than a table or image?
3. **Instructions.** Only after retrieval and content check out, adjust the instructions.

New or edited files need indexing before the agent sees them. Microsoft says it "can take up to several minutes," and the file shows a **Preparing** status in the meantime.

---

## Step 5: Prove the Permissions Hold

Don't launch on trust. Test with two real accounts:

| Tester | Question | Expected result |
|---|---|---|
| A technician (team member, not in HR channel) | "What's the overtime pay rate for office staff?" | No answer from HR documents |
| An HR channel member | Same question | Answer, citing the HR document |

If the technician gets an HR answer, stop. Check who has access to the HR site with **Manage access** on the site, or list the channel members:

```powershell
Get-TeamChannelUser -GroupId $team.GroupId -DisplayName "HR"
```

Also confirm nobody uploaded an HR file directly into the agent (see 3.6). That's the one path that bypasses the library cards.

---

## Step 6: Share It and Launch

Open the agent's **Share** dialog:

1. Add people by **name, group, or email**. Give your readers **Can chat**. Keep **Can edit** for the two or three maintainers. (A group can only be a chat user, never an owner.)
2. Leave **Send notification** checked so people get an email.
3. Select **Copy chat link**, post it in the team's **General** channel, and **pin** the post.

If your admin allows it, there's also an **Org-wide sharing for chat access** toggle. For company-wide distribution with a proper listing, you can submit the agent to your **org catalog**. After admin approval, it appears in the **Built by your org** section of the Agent Store.

Three things to know at launch:

- **It's one-on-one.** People use the agent in Copilot, including Copilot inside Teams. Microsoft lists this as a known limitation: "You can't use agents built in Agent Builder in Teams group or 1:1 chats." So it can't be @mentioned in a channel.
- **Sharing the agent doesn't share the files.** Each person's access comes from the team and channel memberships you set in Step 1. Since we connected whole sites, which Agent Builder doesn't auto-share, Teams membership is the single source of truth. Keep it that way.
- **Removing someone from the agent doesn't remove their file access.** Offboarding happens in Teams membership, not in the agent's share list.

---

## Step 7: Keep It Current with Power Automate

Knowledge bases rarely fail because of the AI. They fail when the documents go stale. Two flows handle that.

### Flow 1: "Ask a Human" Captures Knowledge Gaps

Every question the agent can't answer is a document you haven't written yet.

**Setup:** a Microsoft Form ("Ask a human") with two questions, *What did you ask?* and *What do you need to know?*, with responder names recorded. Put its link in the agent's instructions (rule 2). Then create a list to hold the gaps:

```powershell
Connect-PnPOnline -Url "https://contoso.sharepoint.com/sites/CompanyHandbook" -Interactive -ClientId "<app-id>"

New-PnPList -Title "Knowledge Gaps" -Template GenericList
Add-PnPField -List "Knowledge Gaps" -DisplayName "Asked by" -InternalName "AskedBy" -Type Text -AddToDefaultView
Add-PnPField -List "Knowledge Gaps" -DisplayName "Details" -InternalName "GapDetails" -Type Note -AddToDefaultView
Add-PnPField -List "Knowledge Gaps" -DisplayName "Status" -InternalName "GapStatus" -Type Choice `
             -Choices "New", "Doc written", "Won't cover" -AddToDefaultView
```

Add a **Knowledge Gaps** standard channel to the team for notifications.

**The flow** (Power Automate → **Create → Automated cloud flow**):

1. **Trigger:** Microsoft Forms, *When a new response is submitted*. Form Id: "Ask a human".
2. **Action:** Microsoft Forms, *Get response details*. Form Id: same form. Response Id: the **Response Id** dynamic value from the trigger.
3. **Action:** SharePoint, *Create item*.
   - Site Address: the CompanyHandbook site
   - List Name: Knowledge Gaps
   - Title: the "What did you ask?" answer
   - Details: the "What do you need to know?" answer
   - Asked by: **Responder's Email**
   - Status: New
4. **Action:** Microsoft Teams, *Post message in a chat or channel*.
   - Post as: Flow bot
   - Post in: Channel
   - Team: Company Handbook; Channel: Knowledge Gaps
   - Message: "New knowledge gap from", then the **Responder's Email** dynamic value, then the **What did you ask?** answer from *Get response details*. Insert both with the dynamic content picker rather than typing expressions.

Review the list monthly. The most-asked gaps become your next documents, and the agent gets smarter without anyone touching it.

### Flow 2: The Monday Freshness Check

**The flow** (**Create → Scheduled cloud flow**):

1. **Trigger:** Recurrence. Interval 1, Frequency Week, On these days **Monday**, At these hours **8**, At these minutes **0**, Time zone set to yours. (Set the time zone, or "8:00" means 8:00 UTC.)
2. **Action:** Compose, renamed `Cutoff`:
   ```
   formatDateTime(addDays(utcNow(), -90), 'yyyy-MM-dd')
   ```
3. **Action:** SharePoint, *Get files (properties only)*.
   - Site Address: CompanyHandbook
   - Library Name: Documents
   - Filter Query: `(LastReviewed lt '@{outputs('Cutoff')}') or (LastReviewed eq null)`
   - Top Count: 500

   This is where the clean internal name from Step 2.1 pays off. The `eq null` clause catches files nobody ever reviewed.
4. **Action:** Apply to each, over the **value** output of *Get files*.
   - **Condition:** `empty(items('Apply_to_each')?['DocOwner'])` is equal to `true`
     - **If yes** (no owner): post to the Knowledge Gaps channel: `"@{items('Apply_to_each')?['{FilenameWithExtension}']}" has no owner assigned.`
     - **If no:** Microsoft Teams, *Post message in a chat or channel*. Post as Flow bot, Post in **Chat with Flow bot**, Recipient `items('Apply_to_each')?['DocOwner']?['Email']`, Message:
       ```
       "@{items('Apply_to_each')?['{FilenameWithExtension}']}" hasn't been reviewed in 90+ days.
       Is it still accurate? Open it: @{items('Apply_to_each')?['{Link}']}
       When you've checked it, update the Last reviewed date.
       ```
5. **Repeat steps 3 and 4 for the HR site.** It's a separate site with its own library, so it needs its own *Get files* action.

Turn on failure alerts for both flows (each flow's details page lets the owner get notified on failure). A silent broken flow is worse than no flow, because everyone assumes it's working.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| Agent can't find a document you just added | Still indexing | Wait for the file's **Preparing** status to clear (usually minutes) |
| Agent never finds anything in SharePoint | Restricted SharePoint Search or Restricted Content Discovery | Check Step 0.3 with your admin |
| A user gets no SharePoint-grounded answers at all | No Copilot license and not in a pay-as-you-go policy group | Step 0.1 |
| A specific file is never cited | Scanned PDF, table-heavy, `&` in the name, or very long | Step 2.2 |
| Answers mix up old and new prices | Duplicate documents | Delete the old one; version history keeps it |
| A user asking "what's in the pricing doc?" gets nothing | Questions that reference a file by name retrieve poorly | Ask about the content: "what's the diagnostic fee?" |
| Agent edits aren't showing for users | Changes not published | Select **Update** in Agent Builder |
| HR answers reach non-HR staff | Wrong channel membership, or an HR file uploaded into the agent | Step 5; remove uploads, fix membership |

---

## When You Outgrow Agent Builder

Agent Builder covers the read-only, answer-questions case well. You'll want to move on when you need:

- **A hard lock to your own content.** Agent Builder can't fully block general knowledge. Copilot Studio gives finer control.
- **Actions.** Creating a ticket, looking up an order, filing the "ask a human" request directly. Microsoft's guidance is to **copy the agent to Copilot Studio** to add connectors and workflows.
- **Other sources.** Microsoft 365 Copilot connectors can bring content in from systems like Google Drive, Salesforce, or Confluence.

The agent also follows people into **Copilot in Outlook**, so the refund policy is right there while someone is replying to a customer.

---

## The Real Lesson

Count the steps. The AI is one of seven. The rest is plumbing and discipline:

- licensing that actually covers the people asking
- a site structure where Teams membership *is* the permission model
- documents written so a search engine can find the answer
- a permission test with real accounts before launch
- automation that turns unanswered questions into new documents and nags owners before documents go stale

That's true of nearly every AI project I've built. The model is the easy part. Knowing where your knowledge lives, who should see it, and how it stays current is the real work.

Back at the soccer game, the phone stays in the owner's pocket. The technician asked the handbook.
