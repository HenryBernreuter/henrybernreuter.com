---
date: 2026-06-21 09:00:00
layout: post
title: "FastAPI in One Post"
subtitle: "The framework a freelancer built because he was tired of writing bad APIs slowly"
description: Sebastián Ramírez was a freelance developer in Colombia who needed faster, cleaner API code. What he built in 2018 became the backbone of AI inference infrastructure worldwide.
image: /assets/img/fastapi-hero.png
optimized_image: /assets/img/fastapi-thumb.png
category: tutorial
tags: python fastapi api backend ai tutorial
toc: true
author: henry
---

In 2018, a developer named Sebastián Ramírez was doing freelance API work in Bogotá, Colombia. Client after client, project after project, he was writing the same kinds of web APIs in Python — endpoints that received data, validated it, ran some logic, and returned a response.

He was using Flask, which was fine. But Flask was slow in benchmarks, had no built-in async support, and required a separate library just to validate request data. Every project started with the same boilerplate. Every API he built had inconsistent documentation because documentation was manual and manual things don't get done.

He also noticed that Python had added something called type hints in 3.5. You could now tell Python that a function expected a string, or an integer, or a specific object shape. Most people used them as a signal to their IDE. Sebastián saw something bigger: if you declare what your function expects, the framework should be able to validate input, generate documentation, and serialize output automatically.

He built FastAPI in his spare time. He posted it on GitHub in December 2018. By 2021 it had passed Flask in GitHub stars. By 2023 it was the most popular Python web framework for new projects, and virtually every AI company building an inference API was using it.

---

## The Problem: Python APIs Were Slow to Write and Slow to Run

Flask came out in 2010. It was clean, minimal, and became dominant. But it had not been designed for the world that emerged in the 2010s:

- Single-threaded by default — while it waited for a database query or an external API call, it blocked everything else
- No async support — `async/await` wasn't even in Python yet when Flask was designed
- No built-in data validation — a request could send you anything and Flask would accept it, leaving you to validate it manually
- No auto-generated documentation — you wrote your docs by hand or used add-on libraries that required configuration

Django was the alternative, but Django was a full framework — opinionated about your database, your templates, your project structure. For an API that just needed to receive JSON and return JSON, Django was overhead.

FastAPI solved all of this in one design decision: use Python type hints to do everything automatically.

---

## How FastAPI Works

```python
pip install fastapi uvicorn
```

```python
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class PredictionRequest(BaseModel):
    text: str
    max_tokens: Optional[int] = 512
    temperature: Optional[float] = 0.7

class PredictionResponse(BaseModel):
    result: str
    model: str
    tokens_used: int

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest):
    # Your inference logic here
    result = run_model(request.text, request.max_tokens, request.temperature)
    return PredictionResponse(
        result=result,
        model="my-model-v1",
        tokens_used=len(result.split()),
    )

@app.get("/health")
async def health():
    return {"status": "ok"}
```

That is a complete, production-ready API. What you get automatically:

**Validation** — If a request comes in without `text`, or with `temperature` set to a string, FastAPI rejects it immediately with a clear error message. You wrote no validation code.

**Documentation** — Go to `/docs` and you see a full Swagger UI — every endpoint, every field, every type, every example response. Automatically generated from the type hints you already wrote.

**Async by default** — `async def predict` means this endpoint can handle thousands of concurrent requests without blocking. While one request is waiting for a model to run, other requests proceed.

**Serialization** — The `response_model=PredictionResponse` annotation means FastAPI will validate your response before sending it, strip out any extra fields, and return clean JSON every time.

---

## A Real AI Inference API

Here is the pattern you see in production AI inference services:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from anthropic import Anthropic
import uvicorn

app = FastAPI(title="AI Inference API", version="1.0.0")
client = Anthropic()

class GenerateRequest(BaseModel):
    prompt: str = Field(..., min_length=1, max_length=10000, description="The input prompt")
    model: str = Field(default="claude-haiku-4-5-20251001", description="Model to use")
    max_tokens: int = Field(default=1024, ge=1, le=4096)

class GenerateResponse(BaseModel):
    text: str
    model: str
    input_tokens: int
    output_tokens: int

@app.post("/generate", response_model=GenerateResponse)
async def generate(request: GenerateRequest):
    try:
        message = client.messages.create(
            model=request.model,
            max_tokens=request.max_tokens,
            messages=[{"role": "user", "content": request.prompt}],
        )
        return GenerateResponse(
            text=message.content[0].text,
            model=message.model,
            input_tokens=message.usage.input_tokens,
            output_tokens=message.usage.output_tokens,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/models")
async def list_models():
    return {"models": ["claude-haiku-4-5-20251001", "claude-sonnet-4-6"]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, workers=4)
```

Start this with `python main.py`. Go to `http://localhost:8000/docs`. You have a fully documented, validated, async AI API — built in 40 lines.

---

## Pydantic: The Secret Weapon

The data validation in FastAPI comes from Pydantic, a library Sebastián also contributed to heavily. Pydantic models are Python classes with type annotations that validate themselves:

```python
from pydantic import BaseModel, EmailStr, validator, Field
from typing import List

class UserCreate(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(..., ge=18, le=120)
    tags: List[str] = []

    @validator("username")
    def username_alphanumeric(cls, v):
        assert v.isalnum(), "Username must be alphanumeric"
        return v.lower()

# This works
user = UserCreate(username="Henry123", email="henry@example.com", age=30)

# This raises a ValidationError with a clear message
user = UserCreate(username="h!", email="not-an-email", age=15)
```

You define the shape of your data once, as a Python class, and validation happens automatically — on API input, on database output, anywhere you use the model. No `if request.email is None` scattered through your code.

---

## Why This Still Matters

If you are building any AI application that needs an API — and most do — FastAPI is almost certainly the right choice. The benchmarks consistently put it at or near the top for Python web frameworks. The async support means it handles the high-concurrency, I/O-heavy nature of AI inference well. The auto-documentation means your frontend team, your QA team, and any external integrators can understand your API without asking you.

More importantly: in the AI infrastructure world, FastAPI is ubiquitous. The inference endpoints for Hugging Face models. The APIs behind most LLM-powered tools. The internal services that glue AI systems together. Almost all of it runs on FastAPI.

---

## The One Thing to Remember

**FastAPI took Python type hints — a feature developers were using just to help their IDEs — and made them do validation, documentation, and serialization automatically. It became the fastest way to build correct, well-documented APIs in Python.**

A Colombian freelancer built it because he was tired of writing the same broken boilerplate over and over. The framework he shipped on GitHub on a December evening is now the standard for AI inference APIs worldwide.

---

*Next in this series: TensorFlow — the Google Brain project that put deep learning in production at scale, and how a library that once required a PhD to use became accessible enough for any Python developer to train a neural network.*
