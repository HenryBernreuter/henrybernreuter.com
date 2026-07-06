---
date: 2026-06-17 09:00:00
layout: post
title: "Pandas in One Post"
subtitle: "The spreadsheet a 28-year-old built in Python because Wall Street's tools weren't good enough"
description: Wes McKinney was frustrated by financial data. What he built in 2008 became the single most-used tool in data science.
image: /assets/img/pandas-hero.png
optimized_image: /assets/img/pandas-thumb.png
category: tutorial
tags: python pandas data-engineering tutorial ai
toc: true
author: henry
---

In 2008, a 28-year-old quantitative analyst named Wes McKinney was sitting in front of a Bloomberg terminal at AQR Capital Management, one of the most sophisticated hedge funds in the world. He had more computing power than most universities. He had access to decades of financial data. He had colleagues who were some of the best quants on Wall Street.

He also had a problem that was making him miserable.

Every time he wanted to do something simple — align two time series with different timestamps, merge data from two sources, fill in missing trading days — he had to write pages of custom code that worked once, broke the next time, and could not be reused. Python at the time had NumPy for math and not much else for working with labeled, tabular data. There was no good way to say "give me the row where the date is January 3rd." No fast join. No groupby. No pivot table.

He started building the tool he needed. He called it pandas — short for "panel data," the econometrics term for time series data across multiple subjects. He never expected it to leave finance.

---

## The Problem: Python Had No Spreadsheet

To understand what pandas fixed, you have to understand what working with data looked like before it.

Say you have two datasets: stock prices and company earnings. Both have dates, but the dates don't perfectly align — one is daily, one is quarterly. You want to combine them and compute returns per earnings period.

In NumPy, you have arrays of numbers with no labels. There's nothing to say that row 47 is March 15th. You have to track all of that yourself, in parallel arrays, hoping they stay in sync. It's like working with a spreadsheet where all the column headers have been removed.

What Wes built was a spreadsheet inside Python. A **DataFrame** — a table with labeled rows and labeled columns, where every piece of data knows exactly where it lives. You can slice it, filter it, merge it, reshape it, and run calculations across it. And it's fast, because under the hood it's still NumPy arrays doing the actual math.

That sounds obvious in 2026. In 2008, it was not obvious at all.

---

## What Pandas Actually Does

Pandas gives you two main data structures:

**Series** — a single column of data with an index. Think of it as a labeled array.

**DataFrame** — a table of Series. Rows and columns, both labeled, with the full power of Python behind it.

The operations that matter most:

- **`groupby()`** — split data into groups, apply a function, combine results. The foundation of almost every aggregation.
- **`merge()` and `join()`** — combine two DataFrames like a SQL join, matching on one or more columns.
- **`pivot_table()`** — reshape data the same way you'd use a pivot table in Excel, but in code that can be reproduced.
- **`fillna()` and `dropna()`** — handle missing data without writing loops.
- **Boolean indexing** — `df[df["salary"] > 100000]` — filter rows with an expression that reads like English.

---

## Let's Build Something

Here is a real workflow. We have employee data and we want to analyze salaries by department, spot outliers, and figure out average tenure.

```python
import pandas as pd

# Create a DataFrame directly from a dictionary
data = {
    "name":       ["Alice", "Bob", "Carol", "Dave", "Eve", "Frank"],
    "department": ["Eng",   "Eng", "Sales", "Sales","Eng",  "HR"],
    "salary":     [120000,  95000, 75000,   82000,  140000, 68000],
    "years":      [5,       3,     7,       2,      8,      4],
}
df = pd.DataFrame(data)

# Average salary by department
print(df.groupby("department")["salary"].mean())
```

```
department
Eng      118333.33
HR        68000.00
Sales     78500.00
```

```python
# Filter: only employees earning above $90k
high_earners = df[df["salary"] > 90000]
print(high_earners[["name", "salary", "department"]])
```

```
    name  salary department
0  Alice  120000        Eng
1    Bob   95000        Eng
4    Eve  140000        Eng
```

```python
# Add a derived column: compensation per year of experience
df["salary_per_year"] = df["salary"] / df["years"]

# Sort by it to find the best-compensated relative to experience
print(df.sort_values("salary_per_year", ascending=False)[["name", "salary_per_year"]].head(3))
```

```
    name  salary_per_year
4    Eve         17500.0
0  Alice         24000.0
1    Bob         31666.7
```

Each of those operations — groupby, filter, derived column, sort — is one or two lines. In raw Python, each would be a loop with conditionals. Pandas collapses the mechanical work so you can think about the analysis.

---

## Reading Real Data

Pandas reads almost anything:

```python
# From CSV
df = pd.read_csv("sales_data.csv")

# From Excel
df = pd.read_excel("report.xlsx", sheet_name="Q1")

# From a database (with SQLAlchemy)
df = pd.read_sql("SELECT * FROM transactions WHERE amount > 1000", engine)

# From a URL
df = pd.read_csv("https://example.com/data.csv")
```

And the output:

```python
df.head()          # first 5 rows
df.info()          # column types and null counts
df.describe()      # count, mean, std, min, max for numeric columns
df.shape           # (rows, columns)
df.isnull().sum()  # how many missing values per column
```

That last line — `df.isnull().sum()` — is the fastest way to understand a new dataset. You run it first, before you do anything else.

---

## Why This Still Matters in the Age of AI

Every language model you use was trained on data that was cleaned, organized, and shaped in pandas. Every feature engineering pipeline for a machine learning model ran through it. Every dashboard, every report, every analytics system you have ever used was probably built by someone who started with `pd.read_csv()`.

Pandas did not just become popular. It became the lingua franca of data work in Python. When someone shows you data science code, it almost always starts with `import pandas as pd`.

But the more interesting point for 2026 is what pandas is becoming in the age of LLMs: a tool that feeds context into AI systems.

Modern AI workflows look like this — read raw data with pandas, clean it, extract features, format it as structured context, pass it to Claude or GPT with a question. Pandas handles the data transformation layer. The LLM handles the reasoning layer. Neither replaces the other.

If you are building anything that touches real-world data, you will use pandas. The question is not whether. It is how well.

---

## The One Thing to Remember

**Pandas gave Python a spreadsheet — a labeled, two-dimensional table where every operation on rows and columns is a single function call instead of a loop.**

Wes McKinney built it to survive working at a hedge fund. He open-sourced it in 2009. By 2013 it was the most downloaded Python library in data science. Today it runs on virtually every data team in the world.

The financial data problem he was trying to solve was unglamorous. The solution changed how the world works with data.

---

*Next in this series: Matplotlib — the library John Hunter built in 2003 because his neuroscience students could not afford MATLAB. How a brain scan visualization tool became the foundation of Python's entire plotting ecosystem.*
