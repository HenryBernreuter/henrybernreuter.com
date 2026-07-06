---
date: 2026-06-23 09:00:00
layout: post
title: "Databricks in One Post"
subtitle: "Six Berkeley researchers built Apache Spark to fix Hadoop. Then they built a company to commercialize it. Then the whole industry followed."
description: Databricks was founded by the team that created Apache Spark. The lakehouse architecture they invented is now how most enterprise data and AI work gets done.
image: /assets/img/databricks-hero.png
optimized_image: /assets/img/databricks-thumb.png
category: tutorial
tags: python databricks spark data-engineering ai tutorial
toc: true
author: henry
---

In 2009, a PhD student named Matei Zaharia was sitting in the AMPLab at UC Berkeley, frustrated with Hadoop.

Hadoop was the dominant big data system at the time. The idea was elegant: spread your data across hundreds of machines and process it all in parallel. The reality was painful. Every computation read from disk, wrote to disk, read from disk again. If you wanted to do anything iterative — like training a machine learning model, which requires many passes over the same data — you were reading from disk hundreds of times. On a cluster of spinning hard drives, this was slow enough to make machine learning at scale essentially impractical.

Matei's insight was simple: keep the data in memory between operations. Don't write intermediate results to disk unless you have to. He called the new system Spark — a play on "lightning fast," and a contrast to the "Hadoop" name which referenced an elephant.

He published the Spark paper in 2010. The results were startling: 100x faster than Hadoop for iterative workloads. The machine learning community, which had been struggling with Hadoop's performance, immediately took notice.

In 2013, Matei and five co-founders — Ali Ghodsi, Reynold Xin, Ion Stoica, Patrick Wendell, and Andy Konwinski — left Berkeley and founded Databricks to commercialize Spark as a managed cloud service. They raised $14 million. Apache Spark was donated to the Apache Foundation that same year and became open source.

Today, Databricks is valued at $62 billion. Apache Spark runs on virtually every major cloud platform. The data processing architecture they popularized — the lakehouse — is how most enterprise data teams store and process data for analytics and AI.

---

## The Problem: Data Warehouses and Data Lakes Were Both Wrong

Before the lakehouse, most data organizations were split between two systems that didn't talk to each other well.

**The data warehouse** (Redshift, Snowflake, BigQuery) was fast and queryable but expensive. You stored refined, structured data in it. You ran SQL against it. You paid for every byte stored and every query run.

**The data lake** (S3, ADLS, GCS) was cheap and flexible. You stored raw data there — logs, sensor readings, images, documents, everything. But querying it was slow, and there were no transactions, no schema enforcement, no way to guarantee that what you wrote was what you read.

The lakehouse combined both. You store data cheaply on object storage (like S3), but with a table format layer on top — Delta Lake — that gives you transactions, schema enforcement, and fast query performance. You get data warehouse performance at data lake prices.

Delta Lake, which Databricks created and open-sourced in 2019, is the key. It sits on top of your S3 bucket and adds:

- **ACID transactions** — updates and deletes that don't corrupt your data
- **Schema enforcement** — writing the wrong columns fails with an error rather than silently corrupting the table
- **Time travel** — query any previous version of a table: `SELECT * FROM transactions VERSION AS OF 5`
- **Change data capture** — track what changed between versions

---

## PySpark: The Code

Databricks is built on Apache Spark, which you interact with via PySpark. The API is deliberately similar to pandas, but runs distributed across a cluster.

```python
from pyspark.sql import SparkSession
from pyspark.sql import functions as F

# Create a Spark session (on Databricks this is already available as `spark`)
spark = SparkSession.builder.appName("SalesAnalysis").getOrCreate()

# Read a large CSV from S3 (this distributes across all cluster nodes)
df = spark.read.csv("s3://my-data-bucket/sales/*.csv", header=True, inferSchema=True)

print(f"Total rows: {df.count():,}")
# Total rows: 142,857,920

# Revenue by region — runs in parallel across all nodes
df.groupBy("region") \
  .agg(
      F.sum("revenue").alias("total_revenue"),
      F.count("*").alias("order_count"),
      F.avg("revenue").alias("avg_order_value"),
  ) \
  .orderBy(F.desc("total_revenue")) \
  .show()
```

```
+----------+-------------+-----------+---------------+
|region    |total_revenue|order_count|avg_order_value|
+----------+-------------+-----------+---------------+
|Northeast | 48271093.22 | 1842710   | 26.20         |
|Southeast | 31084821.55 | 1239847   | 25.07         |
|West      | 29443182.10 | 1120943   | 26.27         |
+----------+-------------+-----------+---------------+
```

142 million rows, grouped and aggregated, in seconds — because the computation is running on all cluster nodes simultaneously. The same query in pandas on a single machine would take minutes or crash entirely.

---

## Delta Lake in Practice

```python
# Write a DataFrame as a Delta table
df.write.format("delta").mode("overwrite").save("s3://my-data-bucket/delta/sales")

# Read it back
sales = spark.read.format("delta").load("s3://my-data-bucket/delta/sales")

# Update a record (this is a MERGE — atomic, transactional)
from delta.tables import DeltaTable

sales_table = DeltaTable.forPath(spark, "s3://my-data-bucket/delta/sales")

sales_table.merge(
    source=updates_df,
    condition="sales.order_id = updates.order_id"
).whenMatchedUpdateAll() \
 .whenNotMatchedInsertAll() \
 .execute()

# Time travel: what did this table look like 3 versions ago?
old_sales = spark.read \
    .format("delta") \
    .option("versionAsOf", 3) \
    .load("s3://my-data-bucket/delta/sales")
```

No data warehouse can do a transactional merge into an S3 file. Delta Lake makes it possible.

---

## MLflow: Tracking Experiments

Databricks also created and open-sourced MLflow, which has become the standard for tracking machine learning experiments across the industry.

```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

mlflow.set_experiment("churn-prediction-v2")

with mlflow.start_run():
    # Log parameters
    mlflow.log_param("n_estimators", 200)
    mlflow.log_param("max_depth", 8)

    model = RandomForestClassifier(n_estimators=200, max_depth=8)
    model.fit(X_train, y_train)

    accuracy = accuracy_score(y_test, model.predict(X_test))

    # Log metrics
    mlflow.log_metric("accuracy", accuracy)

    # Log the model itself
    mlflow.sklearn.log_model(model, "model")

    print(f"Run logged. Accuracy: {accuracy:.2%}")
```

Every run gets stored with its parameters, metrics, and model artifact. You can compare 50 experiments in the MLflow UI, see exactly what settings produced what results, and register the best model for deployment.

---

## Why This Matters for AI

Every major AI system needs data. The data has to be collected, cleaned, transformed, and made available to training pipelines. This is the work that happens before any model is trained, and it is most of the work in any real AI project.

Databricks is where that pipeline runs in most large enterprises. The data that feeds foundation model fine-tuning, the feature stores that feed production ML models, the evaluation datasets that test LLM outputs — most of it moves through Spark, gets stored in Delta Lake, and gets tracked in MLflow.

The lakehouse is also where AI results land. When an LLM processes documents and extracts structured data, that data gets written to Delta Lake. When a recommendation model scores every user, those scores go into a Delta table. The outputs of AI connect back to the analytics infrastructure that makes them actionable.

---

## The One Thing to Remember

**Databricks took the distributed compute system that came out of Berkeley, added transactional storage with Delta Lake and experiment tracking with MLflow, and built the data infrastructure layer that most enterprise AI runs on.**

Six researchers needed to iterate on machine learning models faster than Hadoop allowed. What they built to solve that problem is now the platform that processes data for some of the largest AI deployments in the world.

---

*That wraps the core library series. If this helped you understand where these tools came from and why they work the way they do — the origin stories, the problems they solved — that was the goal. Share it with someone who is just starting out.*
