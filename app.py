# ------------------------------------------------------------
# Author: Sushovan Mukherjee
# Description: Vector similarity search demo using FAISS and SentenceTransformers
# ------------------------------------------------------------

import faiss
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

texts = ["This is a sample sentence.", "Here is another example.", "FAISS is great for similarity search."]
embeddings = model.encode(texts)

dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

query = model.encode(["This is a query sentence."])
D, I = index.search(query, k=1)

print("Most similar text:", texts[I[0][0]])
