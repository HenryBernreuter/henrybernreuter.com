---
date: 2026-08-12 09:00:00
layout: post
title: "The Vibe-Coding Trap: What Building an AI Project Manager Taught Me the Hard Way"
subtitle: "I kept believing 'done' meant done. It didn't, and that gap almost cost me the project."
description: A first-person account of building an AI project manager that writes and reviews its own code, and the recurring gap between "the AI says it's fixed" and "it's actually fixed" that nearly sank it.
image: /assets/img/vibe-coding-cautionary-tale.png
optimized_image: /assets/img/vibe-coding-cautionary-tale.png
category: ai-engineering
tags:
  - vibe-coding
  - ai-agents
  - lessons-learned
  - software-engineering
toc: true
author: henry
---

I set out to build an AI project manager. Not a chatbot that answers questions about a
project — an agent that could take a task, write the code, review its own work, deploy it, and
tell me honestly whether it was safe to ship. I called it PMAI. On paper it's a good idea, and
parts of it work. But the story of building it is really a story about a much smaller, much more
dangerous problem: the gap between "the AI says it's done" and "it's actually done." I fell into
that gap more times than I'd like to admit, and I want to write down what it cost me before I
let myself forget.

## The pitch was seductive

The whole appeal of an AI-driven build pipeline is that you stop being the bottleneck. You
describe what you want, an agent writes the code, another agent reviews it, and you just show up
at the end to approve or reject. I built exactly that: a proposal step, a build step, a review
step, and an approval gate in between. Every stage reported back with confident, specific
language — "implemented," "verified," "tests passing." It read like a status update from a
competent engineer. That confidence is exactly what made it dangerous.

Because the code doesn't actually have to be correct to sound confident. It just has to compile,
run once, and not crash on the happy path anyone thought to try. Everything else — the second
click, the retried request, the case nobody wrote a test for — sails right through, wrapped in
the same reassuring "done" language as the parts that were actually solid.

## The bug that kept "working" until it didn't

The clearest example: approving a proposal in PMAI would kick off a build job. The first
approval usually worked fine. But the system generated an internal identifier for that build job
from the *task's* ID, not from anything unique to that specific approval attempt. The first time
you approved something, that ID was fresh, so it worked. But the database was supposed to
guarantee that identifier was globally unique — and if anything about the flow ever ran a second
time against a task that had already produced a terminal job under that same ID, the insert
collided with the database's own uniqueness constraint. The result: a raw 500 error, thrown
*after* the system had already marked the proposal "approved." So the user was left staring at a
crash, while the record underneath them quietly said everything was fine.

That's the part that should scare anyone leaning hard into AI-written code: this wasn't a
one-off typo. It was a structural assumption — "this ID will be unique enough" — that happened to
hold on the first pass through the code and quietly stopped holding the moment real, repeated,
human usage hit it. Every earlier round of "I fixed it" had been true in the narrowest possible
sense: the code ran, the demo worked, the box got checked. Nobody, including me, had asked "what
happens on the second try."

Fixing it for real meant going back to first principles: derive the job's identity from
something that's actually guaranteed to be stable and unique — the proposal itself, not a
recycled task ID — and make the "job already exists" check honest, so that a collision returns
the existing job instead of trying to sneak a duplicate row past a constraint that was always
going to say no. And critically: if starting the job fails anyway, the approval that already
happened must not be left dangling — no proposal marked "approved" with nothing behind it. Small
fix. But it only became obvious once I stopped trusting "it works" and started asking "what did
we actually verify, and what did we just assume?"

## "Deployed" doesn't mean "reachable"

The second lesson was less about code and more about my own habits. After fixing the bug above,
I deployed it and reported back a URL for inspection. It was wrong — I'd pointed at an address
that could never actually be reached from outside the server, when there was already a
perfectly good, previously-established way to reach the test environment that I simply hadn't
checked before speaking. I said "it's deployed" when what I actually meant was "I ran the deploy
steps and didn't check whether the result was reachable the way a person would reach it."

Those are not the same sentence, and conflating them is its own small version of the same trap.
"Deployed" felt like a finish line. It wasn't one. The finish line was "I opened the actual URL a
human would use, and it worked" — and I'd skipped straight past that to declare victory early,
for the second time in the same week, just in a different layer of the stack.

## The moment I almost walked away

Here's the part I don't love writing down: after that fix actually worked — genuinely, verified,
screenshot in hand, no more 500 — a *different* bug showed up immediately behind it. Clicking
"New Task" didn't start a new task. It dropped me back into whatever task had been open before.
Small, annoying, and after a long stretch of "fixed" turning out to mean "fixed until you look
closer," it was the thing that tipped me over. I remember typing something to the effect of "I
think it's time to quit this project." I meant it in the moment.

I didn't quit. But I want to be honest that the exhaustion was real and it wasn't irrational. It
came from a specific, repeated pattern: confident status reports, followed by a real bug the
report hadn't caught, followed by a fix, followed by another confident status report, followed
by another real bug. At some point the fatigue isn't about any single bug — it's about the cost
of never being able to trust the last "done" without re-checking it yourself.

## What "vibe coding" actually costs you

"Vibe coding" — leaning on an AI's fluent, confident description of its own work instead of
independently verifying it — feels fast. It is fast, right up until the bill comes due. The bill
isn't one catastrophic failure. It's a slow accumulation of small, plausible-sounding claims that
turn out to be true only in the narrowest tested case: the first click, not the second; the happy
path, not the retry; the deploy step, not the reachability check. None of those individually feel
like a big deal. Together, they're exhausting in a very specific way, because they erode the one
thing that makes delegation worth anything at all: being able to believe "done" when you hear it.

What actually helped wasn't abandoning AI-assisted development — it was refusing to let "the
agent says it's fixed" be the last word. Ask what was actually run, not just what was claimed.
Ask what happens the second time, not just the first. Ask "reachable by whom, from where" before
accepting "deployed." None of that is exotic engineering discipline — it's the same discipline
good code review has always demanded. The difference is that an AI will produce ten times as
much confident-sounding output per hour as a person will, so the discipline has to scale to match
it, or the gap between "sounds done" and "is done" will quietly fill up with real, load-bearing
bugs.

I'm still building PMAI. It's better than it was, and every one of these lessons is now baked
into how I work with it. But I wanted to write this one down plainly, mistakes included, because
the seductive part of vibe coding isn't the laziness — it's how reasonable it feels to trust a
confident, well-formatted "done" right up until the moment it costs you something real.
