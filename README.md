# 🚀 Vector Database Example

This is a minimal starter project demonstrating vector similarity search using:
- **FAISS** (Facebook AI Similarity Search) for high-speed nearest neighbor search
- **SentenceTransformers** for generating embeddings from text

It’s packaged with a simple Docker environment for easy portability.

---

## 📂 Project structure

```
.
├── app.py            # Main Python script: builds index & queries it
├── requirements.txt  # Python dependencies
├── Dockerfile        # Container setup
├── .gitignore        # Common Python, OS, Docker, VS Code ignores
```
---

## 🔥 Running locally

1. Install Python (>=3.8 recommended)
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the script:
   ```
   python app.py
   ```

---

## 🐳 Running in Docker

Build the image:
```
docker build -t vector-db-basic .
```

Run the container:
```
docker run --rm vector-db-basic
```

---

## 💡 Next ideas for more complex data

- Store embeddings of product descriptions, images, or multi-lingual text.
- Use metadata to filter before similarity search (hybrid search).
- Try different vector sizes / models (e.g. `paraphrase-multilingual-MiniLM-L12-v2`).
- Visualize clusters with t-SNE or PCA.

---

## 📝 License

MIT — use it freely, extend it however you like.

