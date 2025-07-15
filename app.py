# ------------------------------------------------------------
# Author: Sushovan Mukherjee
# Description: Vector similarity search demo using FAISS and SentenceTransformers (cosine similarity, save/load index)
# ------------------------------------------------------------

import faiss
from sentence_transformers import SentenceTransformer
import numpy as np
import os

model = SentenceTransformer('all-MiniLM-L6-v2')

texts = [
    "This is a sample sentence.",
    "Here is another example.",
    "FAISS is great for similarity search."
]
embeddings = model.encode(texts, convert_to_numpy=True)

# Normalize embeddings for cosine similarity
embeddings = embeddings / np.linalg.norm(embeddings, axis=1, keepdims=True)

dimension = embeddings.shape[1]
index_file = "faiss_cosine.index"

if os.path.exists(index_file):
    index = faiss.read_index(index_file)
    print(f"Loaded FAISS index from {index_file}")
else:
    # Use IndexFlatIP for cosine similarity (after normalization)
    index = faiss.IndexFlatIP(dimension)
    index.add(embeddings)
    faiss.write_index(index, index_file)
    print(f"Created and saved FAISS index to {index_file}")

query = model.encode(["do you have another example."], convert_to_numpy=True)
query = query / np.linalg.norm(query, axis=1, keepdims=True)
D, I = index.search(query, k=1)

print("Most similar text:", texts[I[0][0]])
print("Cosine similarity score:", D[0][0])
