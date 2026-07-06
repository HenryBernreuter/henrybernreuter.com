---
date: 2026-07-13 09:00:00
layout: post
title: "AWS Bedrock, Azure AI Foundry, and Vertex AI in One Post"
subtitle: "Amazon, Microsoft, and Google each watched OpenAI turn a research project into a $90 billion company. Then they all built the same thing."
description: AWS Bedrock, Azure AI Foundry, and Google Vertex AI are the three cloud platforms fighting for the enterprise AI market. Here's what they are, how they got here, and how to choose.
image: /assets/img/cloud-ai-platforms-hero.png
optimized_image: /assets/img/cloud-ai-platforms-thumb.png
category: ai-engineering
tags:
  - aws
  - azure
  - gcp
  - bedrock
  - vertex-ai
  - cloud
  - llm
toc: true
author: henry
---

In January 2023, Microsoft announced a ten-year, $10 billion investment in OpenAI and began integrating GPT-4 into every product it owned — Bing, Office, GitHub Copilot, Azure. The bet was audacious and, by the end of that year, it looked prescient. ChatGPT had become the fastest consumer product to reach 100 million users in history. Microsoft's stock climbed. Azure's AI revenue was growing faster than anything else on their platform.

Amazon and Google, two companies that had been working on AI for longer than OpenAI had existed, were suddenly playing catch-up in the perception game.

Amazon had Alexa, which was struggling. Google had LaMDA and the research that had produced much of the theoretical foundation of the transformer architecture — including the 2017 "Attention Is All You Need" paper that made modern LLMs possible. But neither had a ChatGPT moment. Neither had a product that the public recognized as the face of AI.

The enterprise response was fast. All three clouds announced dedicated AI platforms that would let enterprise customers access frontier models, fine-tune open-weight models, build agents, and do it all within the security perimeter of their existing cloud contracts.

AWS launched Bedrock to general availability in April 2023. Google expanded Vertex AI into a full AI platform throughout 2023. Microsoft rebranded and reorganized its Azure AI services into Azure AI Foundry in late 2024.

Three clouds, three platforms, one market. Here's what each actually is.

---

## The Problem They're All Solving

Enterprise AI adoption has a specific set of friction points that none of the direct API providers fully address:

**Security and compliance.** A Fortune 500 company can't just send customer data to the OpenAI API. They need data processing agreements, SOC 2 compliance, HIPAA BAAs, virtual private clouds, audit logs, and access controls. Cloud platforms wrap AI APIs in the enterprise compliance infrastructure companies already have.

**Existing cloud relationships.** Most enterprises already spend millions of dollars on AWS, Azure, or GCP. AI spend under that contract counts toward committed spend discounts. Procurement, legal, and finance all prefer fewer vendors.

**Model diversity.** Enterprises don't want to bet everything on one model provider. They want to be able to swap models, use the right model for each task, and avoid vendor lock-in. All three platforms offer multiple models from multiple providers.

**Integrated tooling.** Storage, compute, monitoring, data pipelines, vector databases — enterprises want AI that connects to the infrastructure they already have, not a new system that requires new integrations.

---

## AWS Bedrock

Amazon's approach was to build a marketplace. Bedrock is less a single AI system and more a managed layer that lets you call foundation models from Anthropic (Claude), Mistral, Meta (Llama), Stability AI, and Amazon's own Nova models — all through a single unified API, all within your AWS account.

```python
import boto3
import json

bedrock = boto3.client("bedrock-runtime", region_name="us-east-1")

# Call Claude via Bedrock — same model, same capability, within AWS
response = bedrock.invoke_model(
    modelId="anthropic.claude-sonnet-4-6",
    body=json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": "Summarize this contract: ..."}
        ]
    })
)

result = json.loads(response["body"].read())
print(result["content"][0]["text"])
```

Bedrock's key features:

**Knowledge Bases** — RAG as a managed service. You point it at an S3 bucket, it chunks and embeds your documents, stores them in a vector database (Amazon OpenSearch Serverless or Aurora pgvector), and handles retrieval automatically. No infrastructure to manage.

**Agents** — Bedrock Agents lets you define tools (Lambda functions) and connect them to a model that decides when to call them. The orchestration loop is managed by AWS. You define the tools; Bedrock handles the rest.

**Guardrails** — content filtering, PII detection, topic blocking — applied consistently across any model in your Bedrock setup.

**Model evaluation** — run your prompts against multiple models and get comparative metrics before committing to a model for production.

Bedrock's weakness is the API — it's not the native Anthropic or OpenAI SDK. You go through `boto3`, which means existing code requires adaptation. The parity with direct API calls is close but not always current; new model features sometimes land on the direct API weeks before Bedrock.

---

## Azure AI Foundry

Microsoft's advantage is the OpenAI relationship. Azure AI Foundry (formerly Azure OpenAI Service) is the only place outside of OpenAI itself where you can access GPT-4o, o1, o3, and the latest OpenAI models with enterprise SLAs.

Azure AI Foundry is Microsoft's unified platform for the full AI development lifecycle — from model access to fine-tuning to deployment to monitoring.

```python
from openai import AzureOpenAI

# Same OpenAI SDK — just pointed at your Azure endpoint
client = AzureOpenAI(
    azure_endpoint="https://your-resource.openai.azure.com/",
    api_key="your-azure-openai-key",
    api_version="2024-02-01"
)

response = client.chat.completions.create(
    model="gpt-4o",          # your deployment name in Azure
    messages=[
        {"role": "user", "content": "Analyze this financial report..."}
    ]
)
print(response.choices[0].message.content)
```

Azure AI Foundry's key features:

**OpenAI model access** — GPT-4o, o-series reasoning models, DALL-E, Whisper — all available with Azure's compliance certifications and private networking.

**Model catalog** — beyond OpenAI, access Llama, Mistral, Phi (Microsoft's own small models), and others. The catalog is growing but OpenAI is the reason most enterprises choose Azure.

**Azure AI Search** — Microsoft's managed vector search and full-text search service, deeply integrated with AI Foundry for RAG pipelines.

**Prompt Flow** — a visual pipeline builder for LLM applications. Not as popular as LangChain among developers, but used by data science teams already embedded in the Microsoft ecosystem.

**Fine-tuning** — Azure offers fine-tuning for GPT-4o and other models with enterprise data that never leaves your Azure tenant.

Azure AI Foundry's weakness is the complexity. Microsoft has reorganized and rebranded its AI services multiple times. If you search for Azure AI documentation, you'll find references to Cognitive Services, Azure OpenAI, Azure ML, and AI Foundry — all referring to overlapping or superseded services. The platform is capable but the learning curve reflects a product built through acquisitions and rapid expansion.

---

## Google Vertex AI

Google's position is unique and uncomfortable. The transformer architecture came from Google Brain. BERT, T5, and foundational research that made the current generation of LLMs possible — Google published most of it. Then a Google spinout (OpenAI was partly funded by people who left Google) turned that research into a product that threatened Google's core business.

Google's response was to ship fast. Gemini — the family of models developed jointly by Google DeepMind — is genuinely competitive with GPT-4 and Claude. Vertex AI is the enterprise platform that makes it accessible.

```python
import vertexai
from vertexai.generative_models import GenerativeModel

vertexai.init(project="your-gcp-project", location="us-central1")

model = GenerativeModel("gemini-1.5-pro")

response = model.generate_content(
    "Analyze this earnings call transcript and identify the three biggest risks mentioned: ..."
)
print(response.text)
```

Vertex AI's key features:

**Gemini model family** — Gemini 1.5 Pro has a 1M token context window, meaning you can feed it an entire codebase, a year of financial documents, or a full book without chunking. This is a genuine capability advantage for certain use cases.

**Model Garden** — Llama, Mistral, and open-weight models alongside Gemini, similar to AWS's approach.

**Grounding** — search grounding connects Gemini to Google Search in real-time, giving the model access to current information without RAG infrastructure.

**Vector Search** — managed vector database service (formerly Matching Engine) with Google's SCANN index under the hood — fast at scale.

**MLOps integration** — Vertex AI has the deepest ML training and deployment infrastructure of the three. If you're training your own models or managing the full ML lifecycle, Vertex AI's tooling is the most mature.

Google's weakness is enterprise trust and go-to-market. Despite its technical capabilities, Google has historically struggled to win enterprise sales the way Microsoft and Amazon have. Enterprises already have Azure or AWS contracts; adding GCP as a primary AI platform requires convincing procurement, legal, and finance of a second cloud relationship.

---

## How to Choose

| | AWS Bedrock | Azure AI Foundry | Google Vertex AI |
|---|---|---|---|
| Best model access | Claude (Anthropic) | GPT-4o, o-series (OpenAI) | Gemini, long-context |
| Existing cloud | Already on AWS | Already on Azure / Microsoft shop | Already on GCP |
| Compliance | Strong | Strongest (Microsoft enterprise) | Strong |
| Open-weight models | Good catalog | Growing | Good catalog |
| RAG / vector search | Knowledge Bases | Azure AI Search | Vector Search |
| ML training/MLOps | Sagemaker (separate) | Azure ML | Best integrated |
| Developer experience | `boto3` — familiar but verbose | OpenAI SDK compatible | Vertex SDK |

**The honest answer:** choose the cloud you're already on. Switching clouds for AI is almost never worth the operational cost unless there's a specific model or capability that only exists on one platform.

If you're genuinely multi-cloud or greenfield, Bedrock is the easiest for teams that use Claude (Anthropic's native SDK experience is better than Bedrock's, but Bedrock's compliance story is strong). Azure wins if OpenAI models are non-negotiable. Vertex wins for long-context workloads or teams that are deep in the Google ecosystem.

---

## The Bigger Picture

These three platforms are not just model APIs. They're bets on where enterprise AI infrastructure is going. All three are racing to offer the same set of capabilities: managed inference, RAG, fine-tuning, agents, monitoring, guardrails, and compliance. The feature sets are converging rapidly.

What each cloud actually owns is its existing customer relationship, its compliance certifications, and its integrated infrastructure story. The AI capabilities are almost table stakes — the real differentiation is whether an enterprise can buy AI in the same purchase order as their storage, networking, and databases.

That's not a very exciting answer for engineers who want to pick the most technically sophisticated platform. But it's the accurate one. Enterprise technology decisions are driven by contracts, relationships, and compliance requirements at least as much as they're driven by benchmarks. The cloud that wins enterprise AI is the cloud that enterprises already trust.