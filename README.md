# 🇧🇩 Multilingual Retrieval-Augmented Generation (RAG) System

This project implements a **basic multilingual RAG system** capable of answering questions in **English** and **Bangla**, using content extracted from a Bengali PDF textbook (HSC 2026 Bangla 1st Paper).

---

## 📚 Features

- Supports both Bangla and English queries
- Extracts Bangla text from PDF
- Splits and chunks the text
- Embeds text using a multilingual transformer
- Uses FAISS for semantic search
- Retrieves relevant answer context from the document

---

## 🔧 Setup Instructions

### 1️⃣ Create and activate a virtual environment (recommended)

bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate

# Run the files in this order:
- extract_text.py
- preprocess.py
- chunker.py
- embedder.py
- vector_store.py
- retriever.py (for manual testing)
- api.py (to test REST API)

🙋 Author
S. M. Nafis Ahmed
Level-1 AI Engineer Assessment — July 2025
