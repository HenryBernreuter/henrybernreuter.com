---
date: 2026-07-14 09:00:00
layout: post
title: "Vector Databases in One Post"
subtitle: "Neural networks learned to turn meaning into math. Then nobody knew where to store it."
description: Vector databases exist because traditional databases can't answer the question 'what is similar to this?' Here's the problem they solved, how they work, and when to use them.
image: /assets/img/vector-databases-hero.png
optimized_image: /assets/img/vector-databases-thumb.png
category: ai-engineering
tags:
  - vector-databases
  - rag
  - embeddings
  - pinecone
  - chroma
  - ai-engineering
toc: true
author: henry
---

<style>.bmc-button img{height: 34px !important;width: 35px !important;margin-bottom: 1px !important;box-shadow: none !important;border: none !important;vertical-align: middle !important;}.bmc-button{padding: 7px 15px 7px 10px !important;line-height: 35px !important;height:51px !important;text-decoration: none !important;display:inline-flex !important;color:#ffffff !important;background-color:#000000 !important;border-radius: 5px !important;border: 1px solid transparent !important;padding: 7px 15px 7px 10px !important;font-size: 28px !important;letter-spacing:0.6px !important;box-shadow: 0px 1px 2px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;margin: 0 auto !important;font-family:'Cookie', cursive !important;-webkit-box-sizing: border-box !important;box-sizing: border-box !important;}.bmc-button:hover, .bmc-button:active, .bmc-button:focus {-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;text-decoration: none !important;box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;opacity: 0.85 !important;color:#ffffff !important;}</style><link href="https://fonts.googleapis.com/css?family=Cookie" rel="stylesheet"><a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/HenryBernreuter"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:5px;font-size:28px !important;">Buy me a coffee</span></a>

In 2013, a team of researchers at Google published a paper called "Distributed Representations of Words and Phrases and their Compositionality." The lead author was Tomas Mikolov. The model was called Word2Vec.

The finding was strange and beautiful: if you trained a neural network to predict which words appeared near other words in a large corpus of text, something unexpected happened. The network's internal representations — the numbers it used to "think" about words — encoded meaning. Not approximately. Structurally.

The famous example: if you took the vector for "king," subtracted the vector for "man," and added the vector for "woman," you got a vector very close to "queen." The math of word relationships had become the math of meaning. Words that meant similar things were stored as similar numbers. You could add, subtract, and compare meanings the way you'd add, subtract, and compare coordinates.

Word2Vec became the foundation for a decade of NLP research. BERT, GPT, and every transformer model that followed built on the same core insight: meaning can be represented as position in a high-dimensional space. A sentence, a paragraph, an image, an audio clip — all of it can be compressed into a vector, a list of floating point numbers, such that things that mean the same thing end up near each other in that space.

This was powerful. It also created a problem nobody had fully anticipated.

Where do you put all those vectors?

---

## The Problem with Traditional Databases

A traditional database is built to answer specific questions:
- "Give me the row where `user_id = 42`" — exact match, O(log n) with an index
- "Give me all rows where `signup_date > 2024-01-01`" — range scan, works on sorted data
- "Give me all rows where `city = 'Austin'`" — index lookup, fast

None of these queries help you find semantic similarity. If you have a million customer support tickets embedded as 1,536-dimensional vectors, and you want to find the 10 tickets most similar to a new incoming ticket, you're asking: "What are the 10 points in 1.5-million-dimensional space closest to this point?"

That's a nearest neighbor search problem. Traditional B-tree indexes can't solve it — they're built for ordered comparisons, not multi-dimensional geometric proximity. A brute-force search (compare every vector to every other vector) is O(n), which at a million documents means a million dot product calculations per query. That gets slow fast.

In 2016, Facebook's AI research team published an open-source library called FAISS (Facebook AI Similarity Search) that introduced efficient approximate nearest neighbor (ANN) algorithms — specifically, HNSW (Hierarchical Navigable Small World graphs). HNSW trades a small amount of recall accuracy for massive gains in query speed. Instead of checking every vector, it navigates a graph structure to find candidates, then checks only those.

FAISS solved the algorithm problem. The infrastructure problem — storing, indexing, updating, and querying billions of vectors reliably, at scale, with a developer-friendly API — was what the vector database companies built.

---

## The Embedding: Where It All Starts

Before understanding vector databases, you need to understand embeddings. An embedding is what you store.

```python
import anthropic

client = anthropic.Anthropic()

# Turn text into a vector — a list of 1,536 floating point numbers
response = client.embeddings.create(
    model="voyage-3",
    input=["The quarterly earnings report showed a 12% increase in recurring revenue."]
)

embedding = response.embeddings[0]
print(f"Vector length: {len(embedding)}")          # 1024
print(f"First 5 values: {embedding[:5]}")
# [-0.0231, 0.0847, -0.0122, 0.0311, -0.0089]
```

That list of numbers is the semantic fingerprint of the sentence. Run the same embedding model on "Q3 recurring revenue grew by 12%" and you'll get a different list of numbers — but the numbers will be geometrically close to the first. The model has learned that these sentences mean the same thing.

Two vectors are similar if the angle between them is small — measured by cosine similarity, which ranges from -1 (opposite) to 1 (identical).

```python
import numpy as np

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# Two semantically similar sentences will have high cosine similarity
sim = cosine_similarity(embedding_1, embedding_2)
# → 0.94 for paraphrases
# → 0.12 for unrelated topics
```

---

## How a Vector Database Works

A vector database stores embeddings alongside their source data and builds an index (usually HNSW) that makes approximate nearest neighbor search fast.

The basic operations:

```python
import chromadb

# Chroma — good for local development and small-to-medium scale
client = chromadb.Client()
collection = client.create_collection("support_tickets")

# Store documents with their embeddings
collection.add(
    documents=["Payment failed on checkout", "Can't log into my account", "Wrong item delivered"],
    embeddings=[embed(t) for t in tickets],
    ids=["ticket-001", "ticket-002", "ticket-003"],
    metadatas=[{"priority": "high"}, {"priority": "medium"}, {"priority": "low"}]
)

# Find the 5 most similar tickets to a new one
results = collection.query(
    query_texts=["Credit card is being declined"],
    n_results=5,
    where={"priority": "high"}  # metadata filter
)
print(results["documents"])
# → ['Payment failed on checkout', ...]
```

```python
from pinecone import Pinecone

# Pinecone — managed, scales to billions of vectors
pc = Pinecone(api_key="your-api-key")
index = pc.Index("support-tickets")

# Upsert (insert or update)
index.upsert(vectors=[
    {"id": "ticket-001", "values": embed("Payment failed on checkout"), "metadata": {"priority": "high"}},
])

# Query
results = index.query(
    vector=embed("Credit card is being declined"),
    top_k=5,
    filter={"priority": {"$eq": "high"}}
)
```

---

## RAG: The Reason Most Teams Have a Vector Database

Retrieval-Augmented Generation is why vector databases went from a niche research tool to mainstream infrastructure almost overnight.

The problem RAG solves: language models have a knowledge cutoff. They don't know your internal documentation, your product database, your customer records, anything that wasn't in their training data. You can't fit your entire knowledge base into a prompt. Context windows are getting longer, but storing millions of documents in context for every query is still prohibitively expensive.

RAG's answer: search first, then answer. Embed your knowledge base, store the embeddings in a vector database, and at query time, retrieve the most relevant chunks and include them in the prompt.

```python
import anthropic

client = anthropic.Anthropic()

def rag_answer(question: str) -> str:
    # 1. Embed the question
    question_embedding = embed(question)

    # 2. Retrieve relevant chunks from the vector database
    results = collection.query(query_embeddings=[question_embedding], n_results=5)
    context = "\n\n".join(results["documents"][0])

    # 3. Answer using retrieved context
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        system="Answer the question using only the provided context. If the answer isn't in the context, say so.",
        messages=[{
            "role": "user",
            "content": f"Context:\n{context}\n\nQuestion: {question}"
        }]
    )
    return response.content[0].text

answer = rag_answer("What's our refund policy for digital products?")
```

The model only sees the 5 most relevant chunks, not the entire documentation site. It answers from what it retrieved. You get answers grounded in your actual content, not model hallucinations.

---

## The Players

**Pinecone** — the first purpose-built vector database company. Edo Liberty, formerly head of Amazon AI Labs and a Yahoo Research scientist, founded it in 2019. Pinecone raised $100 million in 2022 and became the default choice for teams that needed a fully managed vector database that could scale to billions of vectors. The API is simple, the performance is strong, the pricing is opaque at enterprise scale.

**Weaviate** — built in Amsterdam in 2019 by Bob van Luijt. Open-source, self-hostable, with a managed cloud offering. Weaviate's differentiator is that it's a hybrid search database — it supports both vector search and traditional keyword search (BM25) in the same query. Most real-world retrieval benefits from both. Weaviate raised $50 million in 2023.

**Chroma** — the simplest entry point. Jeff Huber (ex-Google Brain) and Anton Troynikov built it in 2022 specifically for AI developers who needed to get started with embeddings quickly. Open-source, runs locally in Python with two lines of code, scales to a managed cloud offering. The default choice for demos, prototypes, and small-to-medium production workloads.

**pgvector** — the Postgres extension that adds vector search to a database you probably already have. Created by Andrew Kane in 2021. If your data is already in Postgres and your scale doesn't demand a dedicated vector store, pgvector is often the right answer — one less system to operate.

**Qdrant** — open-source, Rust-based, fast. Founded in Berlin in 2021. Known for strong filtering performance — when you need to combine vector similarity with complex metadata filters, Qdrant handles it well.

---

## When You Need a Vector Database (and When You Don't)

**Use a vector database when:**
- You're building RAG and your knowledge base is too large for a prompt
- You're building semantic search (not keyword search — meaning-based)
- You're doing recommendations (find items similar to what a user has liked)
- You're doing deduplication on unstructured data (find near-duplicate records)
- Your document corpus changes frequently and you need real-time indexing

**You might not need one when:**
- Your knowledge base is small enough to fit in context — embed the whole thing and skip the retrieval step
- You already have Postgres and pgvector handles your scale
- You only need keyword search — Elasticsearch or even `ILIKE` might do the job
- You're prototyping — Chroma locally is fine, but don't add infrastructure until you know the shape of your problem

The most common mistake is adding a vector database early and spending engineering time on infrastructure that doesn't need to exist yet. Start with the simplest approach — Chroma locally, or just stuffing documents into context — and add a proper vector database when the scale or latency requirements actually demand it.

---

## The Broader Shift

Mikolov's Word2Vec showed that meaning has geometry. What followed — two decades of embedding research, the transformer era, the RAG paradigm — has made that geometry the organizing principle of a new kind of data infrastructure.

Traditional databases organize by equality and order. Vector databases organize by similarity and proximity. They're not replacing relational databases — they're adding a new query type that relational databases were never designed to handle.

The practical upshot is that knowledge, which was previously hard to search at scale, has become queryable. A year of support tickets, a decade of company documentation, a library of research papers — all of it can now be searched not by keywords but by meaning. That shift is what made RAG possible, and RAG is what brought vector databases from research infrastructure to a line in most AI engineering teams' tech stacks.

<style>.bmc-button img{height: 34px !important;width: 35px !important;margin-bottom: 1px !important;box-shadow: none !important;border: none !important;vertical-align: middle !important;}.bmc-button{padding: 7px 15px 7px 10px !important;line-height: 35px !important;height:51px !important;text-decoration: none !important;display:inline-flex !important;color:#ffffff !important;background-color:#000000 !important;border-radius: 5px !important;border: 1px solid transparent !important;padding: 7px 15px 7px 10px !important;font-size: 28px !important;letter-spacing:0.6px !important;box-shadow: 0px 1px 2px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;margin: 0 auto !important;font-family:'Cookie', cursive !important;-webkit-box-sizing: border-box !important;box-sizing: border-box !important;}.bmc-button:hover, .bmc-button:active, .bmc-button:focus {-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;text-decoration: none !important;box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;opacity: 0.85 !important;color:#ffffff !important;}</style><link href="https://fonts.googleapis.com/css?family=Cookie" rel="stylesheet"><a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/HenryBernreuter"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:5px;font-size:28px !important;">Buy me a coffee</span></a>
