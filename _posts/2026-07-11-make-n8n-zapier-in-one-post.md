---
date: 2026-07-11 09:00:00
layout: post
title: "Make, n8n, and Zapier in One Post"
subtitle: "Three teams independently built the same thing: a way to connect software without writing code. Then AI showed up and changed what 'automation' means."
description: Zapier, Make, and n8n each solved the problem of connecting apps without code. Now all three are racing to become the backbone of AI agent infrastructure.
image: /assets/img/automation-platforms-hero.png
optimized_image: /assets/img/automation-platforms-thumb.png
category: ai-engineering
tags:
  - zapier
  - make
  - n8n
  - automation
  - agents
  - no-code
toc: true
author: henry
---

<style>.bmc-button img{height: 34px !important;width: 35px !important;margin-bottom: 1px !important;box-shadow: none !important;border: none !important;vertical-align: middle !important;}.bmc-button{padding: 7px 15px 7px 10px !important;line-height: 35px !important;height:51px !important;text-decoration: none !important;display:inline-flex !important;color:#ffffff !important;background-color:#000000 !important;border-radius: 5px !important;border: 1px solid transparent !important;padding: 7px 15px 7px 10px !important;font-size: 28px !important;letter-spacing:0.6px !important;box-shadow: 0px 1px 2px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;margin: 0 auto !important;font-family:'Cookie', cursive !important;-webkit-box-sizing: border-box !important;box-sizing: border-box !important;}.bmc-button:hover, .bmc-button:active, .bmc-button:focus {-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;text-decoration: none !important;box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;opacity: 0.85 !important;color:#ffffff !important;}</style><link href="https://fonts.googleapis.com/css?family=Cookie" rel="stylesheet"><a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/HenryBernreuter"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:5px;font-size:28px !important;">Buy me a coffee</span></a>

In 2011, Wade Foster was working a marketing job in Columbia, Missouri, manually copying lead data from web forms into spreadsheets. Every time a form came in, he'd copy it. He knew there had to be a better way. He posted in a Hacker News thread asking if anyone wanted to build a startup, met Bryan Helmig and Mike Knoop, and the three of them built Zapier over a weekend at Startup Weekend in Columbia.

The idea was almost embarrassingly simple: if this happens in App A, do that in App B. A new row in Google Sheets triggers a Slack message. A new Stripe payment creates a HubSpot contact. A new Gmail thread opens a Zendesk ticket. They called these automations "Zaps." Users could build them without writing a line of code.

They applied to Y Combinator, got rejected, applied again to the summer 2012 batch, got in. By 2012 they had 600 users. By 2014 the company was profitable. They've never taken venture capital beyond their YC funding — an almost unheard-of choice in the SaaS world — and grew to a reported $140 million ARR by 2021.

A year after Zapier launched, a Czech developer named Ondřej Gazda was building the same thing in Prague — but with a different mental model. Where Zapier thought in linear triggers and actions, Gazda thought in visual flowcharts. He wanted to show the full automation as a diagram you could see and edit. He called it Integromat, launched it in 2012, built it steadily for eight years, then sold it to Celonis in 2020. Celonis rebranded it Make in 2022.

In 2019, a Berlin-based developer named Jan Oberhauser built a third version. He'd been frustrated with Zapier's pricing model — you paid per "task" (each step in each automation), which meant complex workflows got expensive fast. He built n8n as a self-hostable, open-source alternative. You run it on your own server, pay nothing per task, and own your data. He released it under a "fair-code" license — free for self-hosting, paid for cloud hosting. n8n raised $12 million in 2021 and went on to raise significantly more as the AI wave arrived.

Three teams, three approaches, one market. Then AI arrived and changed the question entirely.

---

## The Problem They All Solved

Every SaaS product has an API. Every company uses dozens of SaaS products. Almost none of those products talk to each other by default.

Before automation platforms existed, connecting two systems meant:
- A developer writing custom integration code
- Maintaining that code when either API changed
- Building error handling, retry logic, logging
- Waiting weeks for engineering cycles

Zapier, Make, and n8n solved this by building pre-built connectors — "integrations" or "nodes" — for thousands of popular apps. Salesforce, Gmail, Slack, Notion, Airtable, Stripe, GitHub, HubSpot. They handle the authentication, the API calls, the field mapping, the retry logic. You configure the workflow visually and they run it.

The market for this turned out to be enormous — not just technical users, but marketers, operations teams, founders, anyone who was manually moving data between systems and was tired of it.

---

## The Three Mental Models

Each platform has a fundamentally different way of thinking about automation.

### Zapier: Linear Triggers and Actions

Zapier thinks in a straight line. There is exactly one trigger (the event that starts the workflow) and a sequence of actions that run in order. You can add filters and conditional paths, but the core model is: trigger → action → action → action.

```
[Trigger: New row in Google Sheets]
    → [Filter: Only if column B = "approved"]
    → [Action: Create contact in HubSpot]
    → [Action: Send Slack message to #sales]
```

It's the most constrained model, which makes it the easiest to learn. Zapier's target user is a non-technical marketer or ops person. The interface is optimized for clarity over power.

The tradeoff: complex workflows with loops, branches, or error handling get awkward. Zapier recently added "Tables" (its own database) and AI steps, but it's still fundamentally a linear tool.

### Make (formerly Integromat): Visual Flowchart

Make shows you the entire automation as a visual diagram. Modules are circles connected by arrows. You can see the data flowing through the graph. Multiple triggers, branches, aggregators, iterators, routers — Make exposes more of the underlying plumbing as first-class concepts.

```
[Webhook trigger]
       ↓
  [Router module]
   /           \
[Branch A]   [Branch B]
(type=order) (type=refund)
   ↓               ↓
[Shopify]      [Stripe]
```

Make's mental model is closer to a programming language than Zapier's. You're building a data processing graph, not a checklist. It's more powerful and more complex. The target user is a technically-minded operator or a no-code developer.

### n8n: Code + Visual, Self-Hosted

n8n sits closest to the developer end of the spectrum. It has the visual graph interface of Make, but adds a "Code" node where you can write JavaScript directly when the visual builder isn't expressive enough.

```javascript
// In n8n's Code node — run any JS you need
const items = $input.all();
return items
  .filter(item => item.json.amount > 1000)
  .map(item => ({
    json: {
      ...item.json,
      tier: item.json.amount > 10000 ? "enterprise" : "standard",
      processed_at: new Date().toISOString()
    }
  }));
```

Self-hosting is n8n's core differentiator. Your data never leaves your infrastructure. For teams handling sensitive data — healthcare records, financial information, legal documents — this is often the deciding factor.

n8n also has the most flexible trigger model. Any webhook, any schedule, any event from any system you can reach over HTTP.

---

## The AI Turn

All three platforms have spent the last two years racing to answer the same question: what does workflow automation look like when the steps aren't predetermined?

Traditional automation is if-this-then-that. The logic is written in the workflow. The data flows through it. An AI step makes a classification, generates text, extracts a field — but it's still a fixed pipeline with a fixed shape.

Agentic automation is different. The AI reads the situation and decides what to do. It might call one tool or five. It might loop three times or twenty. The flow isn't determined until runtime.

**Zapier's answer:** Zapier AI (formerly Zapier Central) — a chatbot interface where you describe what you want and an AI builds or runs the automation. Also "AI by Zapier" — a step that calls GPT or Claude mid-workflow.

**Make's answer:** AI modules for Claude, OpenAI, and others, plus Make AI — a natural language interface for building scenarios. Make's visual graph model maps reasonably well to agent workflows because it already supports loops and branches.

**n8n's answer:** LangChain integration built in, dedicated AI agent nodes, and the ability to use the Code node to wire up any LLM SDK directly. n8n has leaned hardest into the developer-facing AI automation market, positioning itself as the infrastructure layer for AI-powered workflows.

---

## Which One to Use

| | Zapier | Make | n8n |
|---|---|---|---|
| Skill level | Non-technical | Technical operator | Developer |
| Pricing model | Per-task | Per-operation | Per-workflow (cloud) / free (self-hosted) |
| Self-hosting | No | No | Yes |
| Data privacy | Data on Zapier's servers | Data on Make's servers | Your servers |
| Connectors | 6,000+ | 1,500+ | 400+ (+ any HTTP) |
| AI integration | Good | Good | Best (code node flexibility) |
| Best for | Marketing/ops teams, simple workflows | Visual power users, complex branching | Developers, sensitive data, AI agent pipelines |

**Choose Zapier** if your users are non-technical and the workflows are straightforward. The polish and the connector library are unmatched.

**Choose Make** if you need visual complexity — multi-branch scenarios, data aggregation, workflows that look like flowcharts — and you want a hosted solution.

**Choose n8n** if you're a developer building AI agent infrastructure, you need self-hosting for compliance or data privacy, or you want to write code when the visual builder isn't enough.

---

## The Real Competition

All three platforms are converging on the same destination: the orchestration layer for AI agents. The future they're each building toward is not "connect Mailchimp to Salesforce" — it's "describe what you want and an AI figures out the steps, calls the tools, loops until done, and reports back."

That puts them in direct competition with LangGraph, with custom agent frameworks, and with each other. The automation platform that figures out how to make agent workflows as easy to build as a Zap will own a very large market.

Jan Oberhauser built n8n because he was frustrated with Zapier's pricing. Wade Foster built Zapier because he was tired of copying spreadsheet rows. What started as tools for moving data between apps has turned into infrastructure for AI systems. Not what anyone planned — but that's usually how the most important software categories develop.

<style>.bmc-button img{height: 34px !important;width: 35px !important;margin-bottom: 1px !important;box-shadow: none !important;border: none !important;vertical-align: middle !important;}.bmc-button{padding: 7px 15px 7px 10px !important;line-height: 35px !important;height:51px !important;text-decoration: none !important;display:inline-flex !important;color:#ffffff !important;background-color:#000000 !important;border-radius: 5px !important;border: 1px solid transparent !important;padding: 7px 15px 7px 10px !important;font-size: 28px !important;letter-spacing:0.6px !important;box-shadow: 0px 1px 2px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;margin: 0 auto !important;font-family:'Cookie', cursive !important;-webkit-box-sizing: border-box !important;box-sizing: border-box !important;}.bmc-button:hover, .bmc-button:active, .bmc-button:focus {-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;text-decoration: none !important;box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;opacity: 0.85 !important;color:#ffffff !important;}</style><link href="https://fonts.googleapis.com/css?family=Cookie" rel="stylesheet"><a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/HenryBernreuter"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:5px;font-size:28px !important;">Buy me a coffee</span></a>
