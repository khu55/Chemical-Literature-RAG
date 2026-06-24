# Chemical Literature RAG

A lightweight Retrieval-Augmented Generation (RAG) system for chemistry and materials science literature.

This project demonstrates how to build a domain-specific literature assistant using:

- PDF parsing
- Text chunking
- Embedding generation
- FAISS vector search
- Local LLM inference with Ollama (Qwen2.5)

The system retrieves relevant passages from scientific papers and uses a local language model to answer user questions based on the retrieved context.

---

## Project Structure

```text
Chemical-Literature-RAG/

├── data/
│   ├── raw/          # Original PDF papers
│   ├── processed/    # Extracted text
│   ├── chunks/       # Chunked documents
│   └── index/        # FAISS index and metadata
│
├── src/
│   ├── parse_pdf.py
│   ├── clean_text.py
│   ├── chunk_text.py
│   ├── build_index.py
│   └── rag_query.py
│
├── requirements.txt
└── README.md
```

---

## Pipeline

```text
PDF
 ↓
Text Extraction
 ↓
Chunking
 ↓
Embedding
 ↓
FAISS Index
 ↓
Retrieve Top-K Chunks
 ↓
Qwen2.5 (Ollama)
 ↓
Answer Generation
```

---

## Installation

Create a Python environment:

```bash
conda create -n chemicalrag python=3.11
conda activate chemicalrag
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Ollama:

```bash
brew install ollama
```

Start Ollama:

```bash
ollama serve
```

Download Qwen:

```bash
ollama pull qwen2.5:3b
```

---

## Build the Knowledge Base

### 1. Parse PDFs

Place papers inside:

```text
data/raw/
```

Run:

```bash
python src/parse_pdf.py
```

---

### 2. Clean Text

```bash
python src/clean_text.py
```

---

### 3. Create Chunks

```bash
python src/chunk_text.py
```

---

### 4. Build Vector Index

```bash
python src/build_index.py
```

---

## Run RAG

```bash
python src/rag_query.py
```

Example:

```text
Question:
What is QM9?
```

Output:

```text
QM9 is a benchmark dataset containing 133,885 small molecules
and is widely used for molecular property prediction tasks.
```

---

## Current Features

- PDF document ingestion
- Semantic chunk retrieval
- FAISS vector search
- Local LLM inference
- Fully offline workflow

---

## Future Improvements

- Citation-aware answers
- Reranking models
- Chemical entity normalization
- SMILES-aware retrieval
- Multi-paper comparison
- Knowledge graph integration

---

## Tech Stack

- Python
- Sentence Transformers
- FAISS
- Ollama
- Qwen2.5
- PyMuPDF

---

## Motivation

Scientific literature is growing rapidly, making it difficult to efficiently locate and summarize relevant information.

This project explores how Retrieval-Augmented Generation (RAG) can be applied to chemistry and materials science papers to improve literature search and question answering while reducing hallucinations.