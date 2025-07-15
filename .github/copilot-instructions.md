# 🧑‍💻 Copilot Instructions for vector_db_basic

## Project Overview
- This project demonstrates vector similarity search using **FAISS** and **SentenceTransformers** in Python.
- The main script (`app.py`) builds a vector index from text, generates embeddings, and performs similarity queries.
- The environment is containerized with Docker for reproducibility and portability.

## Key Files
- `app.py`: Main logic for embedding generation, FAISS index creation, and querying.
- `requirements.txt`: Lists Python dependencies (notably `faiss-cpu`, `sentence-transformers`).
- `Dockerfile`: Builds a minimal image for running the app in isolation.
- `README.md`: Contains setup, usage, and extension ideas.

## Developer Workflows
- **Local run:**
  1. Create a virtual environment (recommended: `.venv`):
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     pip install -r requirements.txt
     ```
  2. Run the script:
     ```
     python app.py
     ```
- **Docker run:**
  1. Build the image:
     ```
     docker build -t vector-db-basic .
     ```
  2. Run the container:
     ```
     docker run --rm vector-db-basic
     ```

## Patterns & Conventions
- All logic is in a single script (`app.py`) for simplicity.
- Embedding model and FAISS index are created at runtime; no persistent storage is used.
- No test suite or CI/CD is present; manual runs are expected.
- No configuration files beyond `requirements.txt` and `Dockerfile`.

## Integration Points
- **External dependencies:**
  - `faiss-cpu` for vector search
  - `sentence-transformers` for text embeddings
- No database or web server integration; all data is in-memory.

## Extending the Project
- To add new data sources, modify `app.py` to load and embed your data.
- To use different models, change the model name in the `SentenceTransformer` instantiation.
- For persistent storage, integrate FAISS index saving/loading.

## References
- See `README.md` for more usage and extension ideas.
- All code and patterns are exemplified in `app.py`.
