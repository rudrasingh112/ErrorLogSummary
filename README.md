# 🛡️ AI-Powered NoSQL Log Monitor

An intelligent log monitoring system built with **FastAPI**, **MongoDB (NoSQL)**, and **LangChain**. This system allows you to ingest logs from various services and use an LLM (OpenAI) to analyze them using natural language.

---

## 🚀 Features

* **Asynchronous Ingestion:** High-performance log ingestion using FastAPI and Motor (Async MongoDB driver).
* **NoSQL Storage:** Schema-less storage in MongoDB Atlas, perfect for varied log metadata.
* **AI Analysis:** Uses LangChain and GPT-4o to analyze log patterns, identify root causes, and suggest fixes.
* **Time-Window Querying:** Analyze logs from specific durations (e.g., the last 30 minutes).
* **Modern LangChain (v1.0+):** Implements the latest LCEL (LangChain Expression Language) for AI orchestration.

---

## 🛠️ Tech Stack

* **Backend:** [FastAPI](https://fastapi.tiangolo.com/)
* **Database:** [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) (NoSQL)
* **AI Framework:** [LangChain](https://www.langchain.com/)
* **LLM:** [OpenAI GPT-4o / GPT-4o-mini](https://openai.com/)
* **Async Driver:** [Motor](https://motor.readthedocs.io/)

---

## 📋 Prerequisites

* Python 3.10+
* MongoDB Atlas Account (or local MongoDB instance)
* OpenAI API Key

---