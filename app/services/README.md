# Services

## query_engine.py
Handles retrieval-augmented question answering against the local Chroma vector database.

- Loads embeddings (MiniLM) and initializes the Chroma store from `chroma/`
- Accepts a user question and performs similarity search
- Builds a compact prompt with the top-k context chunks
- Calls a chat model via OpenRouter and returns the answer and sources

### API usage
The FastAPI app wires this up in `app/main.py`:
- The engine is created on startup (lifespan event)
- POST `/query` receives `{ question: str }` and responds with `{ answer, sources }`

### Configuration
Edit `app/services/query_engine.py`:
- Embedding model: `HuggingFaceEmbeddings(model_name=...)`
- Vector store path: from `app.config.CHROMA_DIR`
- Retrieval parameters: `similarity_search_with_relevance_scores(question, k=3)`
- Prompt template: `PROMPT_TEMPLATE`
- Chat model: `model_name` and `openai_api_base` (OpenRouter)

### Expectations
- The database must be built first by running `python scripts/create_database.py`.
- Sources returned are the text chunks retrieved; tailor the prompt/template to surface metadata as needed.

### Tips
- To change the number of retrieved chunks, adjust `k` in `similarity_search_with_relevance_scores`.
- If you switch embedding models, rebuild the database for consistent vector space alignment.
