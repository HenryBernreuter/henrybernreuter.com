---
date: 2026-07-09
layout: post
title: "Run Your Own Model or Use the API? A Practical Guide"
subtitle: "Part 4: The AI Tooling Decision Framework"
description: The honest cost breakdown for self-hosting LLMs vs. using Claude or another API — privacy, latency, capability, and the math that actually drives the decision.
image: /assets/img/self-hosted-vs-api.png
optimized_image: /assets/img/self-hosted-vs-api.png
category: ai-engineering
tags:
  - llm
  - infrastructure
  - self-hosted
  - claude
  - architecture
toc: true
author: henry
---

<style>.bmc-button img{height: 34px !important;width: 35px !important;margin-bottom: 1px !important;box-shadow: none !important;border: none !important;vertical-align: middle !important;}.bmc-button{padding: 7px 15px 7px 10px !important;line-height: 35px !important;height:51px !important;text-decoration: none !important;display:inline-flex !important;color:#ffffff !important;background-color:#000000 !important;border-radius: 5px !important;border: 1px solid transparent !important;padding: 7px 15px 7px 10px !important;font-size: 28px !important;letter-spacing:0.6px !important;box-shadow: 0px 1px 2px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;margin: 0 auto !important;font-family:'Cookie', cursive !important;-webkit-box-sizing: border-box !important;box-sizing: border-box !important;}.bmc-button:hover, .bmc-button:active, .bmc-button:focus {-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;text-decoration: none !important;box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;opacity: 0.85 !important;color:#ffffff !important;}</style><link href="https://fonts.googleapis.com/css?family=Cookie" rel="stylesheet"><a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/HenryBernreuter"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:5px;font-size:28px !important;">Buy me a coffee</span></a>

This is the infrastructure question that sits underneath every other AI architecture decision. You can't build a pipeline, deploy an agent, or ship a product without deciding: are you calling an API, or are you running a model yourself?

The answer depends on four variables — cost, capability, privacy, and latency — and most teams get at least one of them wrong. This post walks through each variable, puts real numbers on the table, and gives you a framework for making the call.

---

## The Two Options

**API (Claude, GPT, Gemini, etc.):**
You send a request over HTTPS to a hosted model. You pay per token. The provider manages infrastructure, updates, and scaling. You get frontier-level capability with zero ops burden. You also send your data to a third party.

**Self-hosted (Llama, Mistral, Qwen, Phi, etc.):**
You run the model on hardware you control — a GPU server, a cloud instance, an on-prem cluster. You pay for compute. You own the data pipeline end to end. You also own the deployment, monitoring, scaling, and upgrade cycle.

Neither is universally better. The right answer depends on your specific workload.

---

## The Cost Math

This is where most teams make the mistake of looking at per-token API prices and concluding that self-hosting is cheaper at scale. Sometimes it is. Often it isn't, once you account for total cost of ownership.

### API cost model

```
Cost = (input_tokens + output_tokens) × price_per_token
```

Current pricing (approximate, mid-2026):
- Claude Haiku: ~$0.001/1K input, $0.005/1K output
- Claude Sonnet: ~$0.003/1K input, $0.015/1K output
- Claude Opus: ~$0.015/1K input, $0.075/1K output

For a workload processing 10M tokens/day (input + output combined, Sonnet):
```
~10M tokens × $0.009/1K avg = ~$90/day = ~$2,700/month
```

### Self-hosted cost model

An AWS `g5.2xlarge` (A10G, 24GB VRAM) runs about $1.01/hour on-demand, $0.50/hour on a 1-year reserved instance.

A 7B parameter model at 4-bit quantization (Q4) fits on the A10G. At reasonable throughput (150–300 tokens/sec depending on batch size):

```
10M tokens/day ÷ 200 tokens/sec ÷ 86400 sec/day ≈ 0.58 GPUs
→ 1 g5.2xlarge running 14 hours/day
→ $0.50/hr × 14hr = $7/day = ~$210/month
```

On compute alone, self-hosting looks much cheaper at this volume. But that's not the full picture.

### What the compute cost hides

| Hidden cost | Rough estimate |
|------------|----------------|
| Engineer time to deploy & maintain | 0.25–0.5 FTE |
| Monitoring, alerting, incident response | Infrastructure overhead |
| Model upgrade cycle | Every major release requires re-evaluation, re-deployment |
| Quantization quality loss vs. frontier model | Hard to quantify — task-dependent |
| Scaling for traffic spikes | Either over-provision or implement queue |

At a $150K fully-loaded engineer salary, 0.25 FTE = $37,500/year = $3,125/month. That erases most of the compute savings on its own — and that assumes the engineer is efficient and the deployment doesn't have incidents.

**The break-even point** is somewhere in the range of 50–100M tokens/day for a small team, assuming the self-hosted model is capable enough for the task. Below that volume, API is almost always cheaper when you factor in total cost.

---

## The Capability Gap

This is the variable that gets underestimated most often.

Open-weight models have gotten dramatically better. Llama 3.3 70B, Mistral Large, Qwen 2.5 72B — these are genuinely capable models for a wide range of tasks. But frontier API models (Claude Opus, GPT-4o) still outperform them on:

- Complex multi-step reasoning
- Nuanced instruction following
- Tasks that require broad world knowledge
- Long-context coherence (100k+ tokens)
- Code generation for complex or unusual problems

For many production tasks — classification, extraction, summarization, simple Q&A — a well-quantized 7B or 13B model is sufficient. For others, the capability gap is the entire ballgame.

**Test before you commit.** Run your actual production prompts through both options. Measure:
- Task completion rate (does it do what you asked?)
- Output format compliance (does it follow your schema?)
- Error rate on edge cases

If a self-hosted 70B model achieves 94% on your eval and Sonnet achieves 99%, that 5-point gap may or may not matter depending on the task. For a customer-facing feature, it might be disqualifying. For an internal classification job with human review, it might be perfectly fine.

---

## Privacy and Data Residency

This is often the deciding factor for regulated industries — healthcare, finance, legal, government.

**When self-hosting is required:**
- PHI/PII that cannot leave your infrastructure (HIPAA, GDPR)
- Legal documents under confidentiality agreements
- Proprietary IP you won't send to a third party
- Air-gapped environments with no external connectivity

**When API is acceptable:**
- Data covered by the provider's enterprise DPA/BAA
- Non-sensitive workloads where the provider's data handling policies are sufficient
- Cases where you can de-identify or anonymize before sending

Anthropic offers enterprise agreements with data privacy terms that satisfy most compliance frameworks. But if your legal team says the data can't leave your environment, self-hosting is the only path — regardless of cost or capability.

---

## Latency

API latency is a function of network round-trip + model inference time on the provider's infrastructure. For most use cases it's acceptable. For some, it's not.

**API typical latency:**
- Time to first token: 300–800ms (varies by model size and load)
- Streaming: first token fast, full response in 2–10 seconds for typical outputs

**Self-hosted typical latency (g5.2xlarge, 7B Q4):**
- Time to first token: 50–150ms
- Throughput: 150–300 tokens/sec

**When latency drives the decision toward self-hosting:**
- Real-time voice applications where 500ms feels slow
- High-frequency trading or operations where milliseconds matter
- Edge deployments with unreliable network connectivity
- Interactive features where you're streaming completions and API latency creates perceptible lag

For batch workloads and most backend processing, API latency is irrelevant — you're waiting seconds or minutes for jobs to complete regardless.

---

## The Decision Matrix

| Factor | Use API | Self-Host |
|--------|---------|-----------|
| Daily volume | < 50M tokens | > 100M tokens |
| Task complexity | High (reasoning, code, nuance) | Low-medium (classification, extraction) |
| Data sensitivity | Non-sensitive / covered by DPA | PHI, PII, proprietary IP |
| Latency requirement | > 300ms acceptable | < 100ms required |
| Team capacity | Small / no ML infra | Dedicated infra team |
| Model update cadence | Want latest automatically | OK managing upgrade cycle |
| Cost tolerance | Pay for capability | Optimize for compute |

---

## The Hybrid Architecture

In practice, most mature teams end up with a hybrid:

```
[Classification / triage] → small self-hosted model (7B-13B)
[Complex reasoning tasks]  → Claude Sonnet/Opus via API
[High-volume extraction]   → self-hosted 70B or distilled model
[Customer-facing chat]     → Claude via API (capability + safety)
[Sensitive data pipeline]  → self-hosted (data never leaves)
```

Route by task type. Use the cheapest capable model for each workload. Don't make a single binary choice for your entire stack.

### Tools for self-hosting

| Tool | Best for |
|------|---------|
| Ollama | Local development, single machine |
| vLLM | Production serving, high throughput, batching |
| llama.cpp | CPU inference, edge deployments, minimal setup |
| Hugging Face TGI | Docker-based, good observability |
| AWS Bedrock (custom models) | Managed self-hosting on AWS infra |

### Calling Claude from your own code

```python
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

response = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Your prompt here"}
    ]
)

print(response.content[0].text)
```

That's the full integration. The complexity lives in your prompt design and pipeline architecture, not in the SDK call itself.

---

## Making the Call

Start with the API. The default choice for a new project is to call the API — lower risk, higher capability, no ops burden, pay-as-you-go scaling. You can always migrate high-volume, low-complexity workloads to self-hosting once you have:

1. A production eval that shows a self-hosted model is capable enough for the task
2. Volume that makes the compute economics work
3. Engineering bandwidth to own the deployment

Don't self-host prematurely. The capability ceiling of open-weight models is rising fast, but the ops burden of running your own inference infrastructure is real and ongoing. Earn the complexity.

---

## Summary

| Decision driver | Points toward API | Points toward self-hosting |
|----------------|-------------------|--------------------------|
| Volume | Low-medium | Very high |
| Capability need | High | Medium-low |
| Data privacy | Flexible | Strict |
| Latency | Tolerant | Strict |
| Team size | Small | Has infra capacity |
| Time to ship | Fast | Longer |

The AI tooling stack is not a single decision — it's a set of per-workload decisions. Pick the right tool for each job, measure the tradeoffs with real data, and move to self-hosting when the math and the requirements actually support it.

<style>.bmc-button img{height: 34px !important;width: 35px !important;margin-bottom: 1px !important;box-shadow: none !important;border: none !important;vertical-align: middle !important;}.bmc-button{padding: 7px 15px 7px 10px !important;line-height: 35px !important;height:51px !important;text-decoration: none !important;display:inline-flex !important;color:#ffffff !important;background-color:#000000 !important;border-radius: 1px solid transparent !important;padding: 7px 15px 7px 10px !important;font-size: 28px !important;letter-spacing:0.6px !important;box-shadow: 0px 1px 2px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;margin: 0 auto !important;font-family:'Cookie', cursive !important;-webkit-box-sizing: border-box !important;box-sizing: border-box !important;}.bmc-button:hover, .bmc-button:active, .bmc-button:focus {-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;text-decoration: none !important;box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;opacity: 0.85 !important;color:#ffffff !important;}</style><link href="https://fonts.googleapis.com/css?family=Cookie" rel="stylesheet"><a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/HenryBernreuter"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:5px;font-size:28px !important;">Buy me a coffee</span></a>
