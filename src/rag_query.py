from sentence_transformers import SentenceTransformer
import faiss
import pickle
import numpy as np
import ollama

# 1. 加载模型
model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

# 2. 加载FAISS
index = faiss.read_index(
    "data/index/faiss.index"
)

# 3. 加载chunk内容
with open(
    "data/index/chunks.pkl",
    "rb"
) as f:
    chunks = pickle.load(f)

# 4. 输入问题
query = input("Question: ")

# 5. 问题转向量
query_embedding = model.encode(
    [query],
    convert_to_numpy=True
).astype("float32")

# 6. 搜索Top5
distances, indices = index.search(
    query_embedding,
    k=5
)
# 取回Top5文本

context = "\n\n".join(

    [
        chunks[idx]["text"]
        for idx in indices[0]
    ]

)

prompt = f"""
You are a chemistry research assistant.
Answer the question using ONLY the context below.
Context:
{context}
Question:
{query}
"""

#response
response = ollama.chat(

    model="qwen2.5:3b",
    messages=[

        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response["message"]["content"])