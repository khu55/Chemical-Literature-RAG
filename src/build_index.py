from pathlib import Path
import json
import pickle

import faiss
import numpy as np
from sentence_transformers import SentenceTransformer


chunk_path = Path("data/chunks/chunks.json")
index_dir = Path("data/index")
index_dir.mkdir(parents=True, exist_ok=True)

with open(chunk_path, "r", encoding="utf-8") as f:
    chunks = json.load(f)

texts = [chunk["text"] for chunk in chunks]

model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

embeddings = model.encode(
    texts,
    show_progress_bar=True,
    convert_to_numpy=True
)

embeddings = embeddings.astype("float32")

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

faiss.write_index(index, str(index_dir / "faiss.index"))

with open(index_dir / "chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

print(f"Built FAISS index with {len(chunks)} chunks")
print(f"Embedding dimension: {dimension}")