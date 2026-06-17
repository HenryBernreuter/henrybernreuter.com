---
date: 2026-06-18 09:00:00
layout: post
title: "Matplotlib in One Post"
subtitle: "The neurologist who couldn't afford MATLAB and built Python's entire plotting foundation instead"
description: John Hunter was analyzing brain scans on a research budget. What he built to replace a $1,000 license became the bedrock of Python data visualization.
image: /assets/img/matplotlib-hero.png
optimized_image: /assets/img/matplotlib-thumb.png
category: tutorial
tags: python matplotlib data-visualization tutorial ai
toc: true
author: henry
---

In 2003, a neurobiologist named John Hunter was working as a postdoctoral researcher at the University of Chicago, analyzing epilepsy patient data. He had EEG recordings from brain electrodes, thousands of time points, multiple channels per patient. He needed to plot it all, look at it, understand what was happening in the brain during a seizure.

The tool that scientists used for this kind of work was MATLAB. MATLAB was good. It had excellent plotting, good numerical computing, and the whole scientific community had built up years of code in it.

It also cost over a thousand dollars per seat.

John was running a research lab. His graduate students did not have a thousand dollars. The university had a limited number of MATLAB licenses, which meant waiting in line to use them. For a neuroscientist who needed to look at data constantly, this was untenable.

He decided to recreate the MATLAB plotting experience in Python, which was free. He called it matplotlib — short for "MATLAB-like plotting library." He open-sourced it in 2003 and posted it to a mailing list. The response was immediate.

By the time he died of a heart attack in 2012 at age 44, matplotlib had become the backbone of scientific visualization in Python. Every major plotting library — seaborn, plotly, pandas plotting — was either built on top of it or heavily inspired by it. His obituary in the Python community drew tributes from scientists and engineers around the world.

---

## The Problem: Python Had No Way to Show Data

NumPy could crunch numbers. Pandas could organize them into tables. But once you had results, how did you look at them?

Before matplotlib, you would write your Python analysis, get some numbers, copy them into Excel, make a chart there, wonder why it looked wrong, fix it, copy again. The data lived in Python. The visualization lived somewhere else. Every time something changed, you started over.

Matplotlib closed the loop. Your data, your analysis, and your charts all lived in the same script. Change the data, re-run the script, the chart updates. This sounds basic. At the time, for scientists used to MATLAB, it was exactly what they needed.

---

## How Matplotlib Works

Matplotlib has two ways to draw things. One is the quick way. One is the right way.

**The quick way — the `pyplot` interface:**

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.show()
```

This is the interface that looks like MATLAB. You call `plt.something()` functions one after another and matplotlib keeps a running state. Good for quick exploration.

**The right way — the object-oriented interface:**

```python
fig, ax = plt.subplots()

ax.plot(x, y, label="sin(x)", color="#7c3aed", linewidth=2)
ax.set_title("Sine Wave")
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
ax.legend()

plt.tight_layout()
plt.savefig("sine.png", dpi=150)
```

You create a `Figure` (the whole canvas) and one or more `Axes` (each individual plot panel). Then you call methods on those objects. This approach is cleaner when you have multiple subplots or are building anything beyond a single quick chart.

---

## A Real Example: Comparing Models

Here is the kind of chart you build constantly in data science — comparing how multiple models perform across training iterations.

```python
import matplotlib.pyplot as plt
import numpy as np

epochs = np.arange(1, 21)
train_loss = 1.0 * np.exp(-0.15 * epochs) + np.random.normal(0, 0.01, 20)
val_loss   = 1.0 * np.exp(-0.12 * epochs) + np.random.normal(0, 0.02, 20)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Left panel: loss curves
axes[0].plot(epochs, train_loss, label="Training Loss",   color="#2563eb", linewidth=2)
axes[0].plot(epochs, val_loss,   label="Validation Loss", color="#dc2626", linewidth=2, linestyle="--")
axes[0].set_title("Loss Over Training")
axes[0].set_xlabel("Epoch")
axes[0].set_ylabel("Loss")
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Right panel: accuracy bar chart
models = ["Logistic Reg.", "Decision Tree", "Random Forest", "SVM"]
scores = [0.974, 0.939, 0.965, 0.974]
colors = ["#2563eb" if s == max(scores) else "#94a3b8" for s in scores]

axes[1].bar(models, scores, color=colors)
axes[1].set_title("Model Accuracy Comparison")
axes[1].set_ylabel("Accuracy")
axes[1].set_ylim([0.9, 1.0])
axes[1].tick_params(axis="x", rotation=15)

for i, (model, score) in enumerate(zip(models, scores)):
    axes[1].text(i, score + 0.001, f"{score:.1%}", ha="center", fontsize=9)

plt.suptitle("Model Performance Summary", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig("model_comparison.png", dpi=150, bbox_inches="tight")
```

That produces a two-panel figure: training curves on the left, accuracy comparison on the right — the kind of thing that goes in a report or a presentation. Clean, labeled, saved to a file.

---

## The Common Chart Types

```python
# Line chart
ax.plot(x, y)

# Scatter plot
ax.scatter(x, y, alpha=0.6, c=colors)

# Bar chart
ax.bar(categories, values)

# Histogram
ax.hist(data, bins=30, edgecolor="white")

# Heatmap (via imshow)
ax.imshow(matrix, cmap="viridis", aspect="auto")

# Box plot
ax.boxplot([group1, group2, group3])
```

One set of building blocks. Every type of chart follows the same pattern — create axes, call a method, set labels.

---

## Why This Still Matters

Seaborn is more beautiful. Plotly is interactive. Altair is more elegant. They all exist, and they are all good.

But matplotlib is still what you reach for when you need exact control. Seaborn is built on top of it. Pandas `.plot()` method is a wrapper around it. When the higher-level libraries don't give you exactly what you need, you drop down to matplotlib and draw it yourself.

In AI workflows, matplotlib is where you visualize what your models are actually doing. Loss curves. Confusion matrices. Feature importance charts. The distribution of your training data vs. your production data. Attention maps from transformer models. All of it drawn with the same library John Hunter built to replace his $1,000 MATLAB license.

The deeper point is that visualization is not optional. It's how you find out that your model is learning the wrong thing, that your data has a leak, that the two groups you thought were similar are completely different. The chart reveals what the numbers obscure.

---

## The One Thing to Remember

**Matplotlib is the canvas. Every Python visualization — whether you know it or not — is either running on it or running next to it.**

John Hunter built it for neuroscientists who couldn't afford commercial software. It outlasted MATLAB in the Python ecosystem, outlasted the early competitors, and quietly became infrastructure for scientific computing worldwide.

He never saw its full impact. But every data scientist who has typed `plt.show()` and watched a chart appear owes him something.

---

*Next in this series: LangChain — the project Harrison Chase open-sourced six weeks after ChatGPT dropped, and how a single idea about "chaining" AI calls together changed how every developer builds with language models.*
