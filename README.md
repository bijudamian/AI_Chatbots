# AI Chatbots

> Building and documenting RAG-based AI chatbots designed to explore and interact with historical data

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge)](https://langchain.com)
[![Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev)
[![MIT License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

## Overview

A progressive series of Python chatbot implementations — from a simple LLM wrapper to full RAG (Retrieval-Augmented Generation) pipelines. Each script builds on the last, making this a perfect learning resource for AI chatbot development.

## Implementations

| File | Description |
|---|---|
| `00_Basic_Chatbot.py` | Simple Gemini chatbot with single-turn responses |
| `01_Chatbot_with_history.py` | Multi-turn chatbot with conversation memory |
| `02_rag_from_text.py` | RAG pipeline using plain text as knowledge source |
| `03_rag_from_pdf.py` | RAG pipeline with PDF ingestion via document loaders |

## Tech Stack

- **Language**: Python 3.10+
- **LLM**: Google Gemini (via LangChain)
- **Vector Store**: FAISS / Chroma
- **Document Loading**: LangChain document loaders
- **Embeddings**: Google Generative AI Embeddings

## Getting Started

```bash
# Clone the repo
git clone https://github.com/bijudamian/AI_Chatbots.git
cd AI_Chatbots

# Install dependencies
pip install -r requirements.txt

# Set your Gemini API key
export GOOGLE_API_KEY="your-key-here"

# Run any implementation
python 00_Basic_Chatbot.py
python 03_rag_from_pdf.py
```

## Learning Path

```
00_Basic_Chatbot.py
      ↓
01_Chatbot_with_history.py   ← adds memory
      ↓
02_rag_from_text.py          ← adds retrieval
      ↓
03_rag_from_pdf.py           ← adds PDF support
```

## License

MIT © [Biju Damian](https://github.com/bijudamian)
