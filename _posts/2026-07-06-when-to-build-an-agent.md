---
date: 2026-07-06
layout: post
title: "When to Build an Agent (And When You're Overcomplicating It)"
subtitle: "Part 1: The AI Tooling Decision Framework"
description: A practical decision framework for choosing between raw API calls, orchestration frameworks like LangChain, and full agentic systems — with real examples from production.
image: /assets/img/when-to-build-an-agent.png
optimized_image: /assets/img/when-to-build-an-agent.png
category: ai-engineering
tags:
  - agents
  - langchain
  - llm
  - architecture
toc: true
author: henry
---

<style>.bmc-button img{height: 34px !important;width: 35px !important;margin-bottom: 1px !important;box-shadow: none !important;border: none !important;vertical-align: middle !important;}.bmc-button{padding: 7px 15px 7px 10px !important;line-height: 35px !important;height:51px !important;text-decoration: none !important;display:inline-flex !important;color:#ffffff !important;background-color:#000000 !important;border-radius: 1px solid transparent !important;padding: 7px 15px 7px 10px !important;font-size: 28px !important;letter-spacing:0.6px !important;box-shadow: 0px 1px 2px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;margin: 0 auto !important;font-family:'Cookie', cursive !important;-webkit-box-sizing: border-box !important;box-sizing: border-box !important;}.bmc-button:hover, .bmc-button:active, .bmc-button:focus {-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;text-decoration: none !important;box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;opacity: 0.85 !important;color:#ffffff !important;}</style><link href="https://fonts.googleapis.com/css?family=Cookie" rel="stylesheet"><a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/HenryBernreuter"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:5px;font-size:28px !important;">Buy me a coffee</span></a>

The most common mistake I see engineers make when adding AI to a product is jumping straight to agents. They read about autonomous AI, watch a demo of Claude browsing the web and filing Jira tickets, and immediately start wiring up tool loops and memory systems for what should have been a single API call.

The second most common mistake is the opposite: calling the raw API with a 2,000-token prompt, wondering why it keeps hallucinating, and blaming the model when the real problem is that no architecture can save a task that needs state, retrieval, or multiple reasoning steps compressed into one shot.

This series is a decision framework for the space between those two failure modes. Before we talk about LangChain, LlamaIndex, AutoGen, or any framework — we need to agree on when each layer of abstraction earns its keep.

---

## The Three Layers

Think of AI tooling as three concentric rings:

**Ring 1 — Raw API call.** You send a prompt, you get a completion. One HTTP request. No memory, no tools, no loops.

**Ring 2 — Orchestration / chains.** You string multiple calls together, inject retrieved context, manage prompt templates, and route between steps with logic you control. LangChain, LlamaIndex, and a dozen custom `run_pipeline()` functions live here.

**Ring 3 — Agents.** The model decides what to do next. It picks tools, executes them, reads the output, and loops until it either completes the task or hits a limit you set. You are no longer writing the control flow — you are defining the environment and the boundaries.

Most real problems belong in Ring 1 or Ring 2. Ring 3 is the right answer less often than the hype suggests, and the wrong answer is more expensive than you think.

---

## When Ring 1 Is Enough

A raw API call is the right choice when all of the following are true:

- **The task fits in a single prompt.** All the context the model needs can be assembled before the call.
- **The output is terminal.** You're not feeding the result back into another LLM step.
- **Failure is cheap.** A bad generation means you retry or surface an error — not that you've executed a half-finished multi-step workflow with side effects.
- **You need latency guarantees.** A 400ms response from a single `chat.completions.create()` call is hard to match once you add orchestration overhead.

**Examples that belong in Ring 1:**
- Summarizing a user-submitted document
- Classifying support tickets into categories
- Generating product description copy from a spec
- Answering a question from a static knowledge base you've already stuffed into the prompt
- Extracting structured data from a blob of text into a schema

The mistake here isn't using the raw API — it's under-engineering the *prompt*. A good system prompt, well-structured few-shot examples, and explicit output formatting instructions can handle a surprising amount of complexity. Before you add a framework, ask whether the problem is actually a prompting problem.

---

## When You Need Ring 2

Add orchestration when your task has structure that the model alone shouldn't decide at runtime:

- **Multi-step reasoning with intermediate results.** You want to control the steps — the model shouldn't improvise them. Example: extract entities from a document, then look each one up in a database, then synthesize a report. That's three deterministic steps with a model at the center of each.
- **Retrieval-augmented generation (RAG).** The context doesn't fit in the prompt, so you retrieve relevant chunks first. The retrieval logic is yours — the model just reads what you hand it.
- **Prompt routing.** Different types of input need different prompts, personas, or even different models. You write the router; the model just handles the leaf nodes.
- **Output validation and retry loops.** The model produces JSON that fails your schema validator, so you re-prompt with the error message. This is orchestration, not agency — you're in control of every iteration.

**Examples that belong in Ring 2:**
- A chatbot with conversation history and a connected knowledge base
- A data pipeline that extracts, transforms, and loads via LLM calls
- A code review tool that runs static analysis first, then passes findings to the model
- A content moderation system that classifies, routes, and escalates

LangChain, LlamaIndex, and similar frameworks are well-suited here — *if* you actually need their abstractions. A chain, a retriever, and a memory module cover most Ring 2 cases. The trap is pulling in a full framework when three functions and a loop would do the same job with less indirection.

> **Rule of thumb:** If you can draw your pipeline as a static flowchart before running it, you're in Ring 2. The arrows don't change based on model output.

---

## When You Actually Need an Agent

An agent is the right tool when the **control flow itself** is unknown until runtime. The model has to decide what to do next because you genuinely can't enumerate the steps in advance.

Signs you need Ring 3:

- **Open-ended tasks with variable sub-problems.** "Research this company and tell me if we should partner with them" could require 2 searches or 20 depending on what surfaces.
- **Tool selection based on content.** The model needs to read something, decide it needs more information, and go get it. The decision is data-dependent in a way that's hard to pre-specify.
- **Long-horizon tasks with checkpoints.** The work unfolds over time, and intermediate results meaningfully change what happens next.
- **Environments, not pipelines.** You're giving the model a workspace — a file system, a browser, a code interpreter — and asking it to accomplish a goal within it.

**Examples that actually need agents:**
- A software engineering assistant that can read a codebase, run tests, identify failing cases, write a fix, and verify it
- A research assistant that queries multiple sources, identifies gaps, and decides when it has enough to answer
- An operations agent that monitors a system, identifies anomalies, and takes corrective action
- A customer-facing assistant that looks up account state, files support tickets, and schedules callbacks — all in one turn

The cost of getting this wrong is real. Agents are harder to debug, harder to make deterministic, more expensive per task, and more likely to produce hard-to-reverse side effects. Every tool call is a potential failure point, and failure at step 7 of 12 is worse than failure at step 1 of 1.

---

## The Decision Checklist

Before picking your tooling, answer these five questions:

| Question | If Yes | If No |
|----------|--------|-------|
| Does all required context fit in one prompt? | Ring 1 | Ring 2+ |
| Is the sequence of steps fixed before runtime? | Ring 2 | Ring 3 |
| Does the model need to pick its own tools? | Ring 3 | Ring 1-2 |
| Are there side effects that can't be undone? | Minimize agent scope | Agents are safer here |
| Is latency a hard requirement? | Raw API or short chains | Agents are OK |

---

## What About Frameworks?

LangChain, LlamaIndex, AutoGen, CrewAI — these aren't "agent vs. not-agent" tools. They span Ring 2 and Ring 3, and most of them handle both. The question of whether to use a framework is separate from whether to use an agent, and it deserves its own post.

For now: frameworks are abstractions. Abstractions earn their cost when they handle complexity you don't want to re-implement — retrieval pipelines, memory backends, tool registries, streaming, tracing. They become a liability when they obscure what's actually happening, make debugging harder, or add 10 dependencies to solve a problem that needed 30 lines.

The next post in this series covers exactly that: when frameworks accelerate you, when they slow you down, and how to evaluate them against writing the orchestration yourself.

---

## Summary

- **Ring 1 (raw API):** single prompt, terminal output, latency-sensitive, no state
- **Ring 2 (orchestration):** fixed multi-step pipelines, RAG, routing, retry logic — frameworks optional
- **Ring 3 (agents):** dynamic control flow, open-ended tasks, model-selected tools, environment interaction

The right architecture is the simplest one that actually solves the problem. Start in Ring 1 and move outward only when you hit a genuine wall. Most walls are prompting problems in disguise.

<style>.bmc-button img{height: 34px !important;width: 35px !important;margin-bottom: 1px !important;box-shadow: none !important;border: none !important;vertical-align: middle !important;}.bmc-button{padding: 7px 15px 7px 10px !important;line-height: 35px !important;height:51px !important;text-decoration: none !important;display:inline-flex !important;color:#ffffff !important;background-color:#000000 !important;border-radius: 1px solid transparent !important;padding: 7px 15px 7px 10px !important;font-size: 28px !important;letter-spacing:0.6px !important;box-shadow: 0px 1px 2px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;margin: 0 auto !important;font-family:'Cookie', cursive !important;-webkit-box-sizing: border-box !important;box-sizing: border-box !important;}.bmc-button:hover, .bmc-button:active, .bmc-button:focus {-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;text-decoration: none !important;box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;opacity: 0.85 !important;color:#ffffff !important;}</style><link href="https://fonts.googleapis.com/css?family=Cookie" rel="stylesheet"><a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/HenryBernreuter"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:5px;font-size:28px !important;">Buy me a coffee</span></a>