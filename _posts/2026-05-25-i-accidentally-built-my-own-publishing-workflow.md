---
date: 2026-05-25 09:00:00
layout: post
title: I Accidentally Built My Own Publishing Workflow
subtitle: It started as "let me make posting easier"
description: How trying to simplify my blog turned into a full AI-powered publishing tool I actually use every day.
image: /assets/img/workflow-hero.png
optimized_image: /assets/img/workflow-thumb.png
category: blog
tags: python ai automation workflow
toc: false
author: henry
---

I was trying to make it easier to write blog posts.

That's it. That was the whole plan.

I had a Jekyll site, a list of topics I wanted to write about, and zero desire to manually create a file, fill in front matter, name it correctly, and remember the date format every single time.

So I wrote a PowerShell script. You give it a topic, it creates the file, pre-fills the front matter, drops you into the right folder. Done in 30 seconds instead of 3 minutes.

Then I thought, what if it also drafted the content?

So I wired it into the Claude API. Now you give it a topic and an optional outline, and it comes back with a full 700-word draft. Title, subtitle, tags, description — all suggested automatically.

Then I thought, what if I didn't have to open a terminal at all?

So I built a UI. A dark-themed desktop app in Python. You type in your topic, hit Generate, and a draft appears in an editable text box. You clean it up, browse for your header image, hit Publish — and it writes the file, copies the images, runs `git commit`, and pushes to the repo. Netlify picks it up and deploys automatically.

Start to published: under 10 minutes.

---

What I thought I was building: a shortcut.

What I actually built: a content system that fits exactly how I work.

I didn't plan any of this. It grew one problem at a time. Each step felt obvious in the moment — the next friction point became the next thing to remove.

That's the thing about building with AI tools. The barrier between "I wish this existed" and "this now exists" has collapsed. You don't need a team. You don't need a sprint. You need an afternoon and a clear picture of what's annoying you.

If you can think it, you can build it.

More importantly, you can build things that fit how *you* work — not how some product manager decided you should work.

---

The stack, if you're curious:

- **Python + tkinter** for the desktop UI
- **Claude API** (claude-sonnet-4-6) for drafting
- **Jekyll** for the site
- **git** for version control
- **Netlify** for auto-deployment

The whole tool is about 500 lines of Python. It lives in the same repo as the site. It's not a product — it's infrastructure for one person, built to remove every excuse not to write.

That's the kind of automation worth building first.
