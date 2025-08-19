# Scripts

## create_database.py
Builds the local vector database from documents in the `data/` directory.

- Recursively discovers files in `data/`
- Loads PDF, TXT, and DOCX formats
- Splits documents into chunks for retrieval
- Embeds and persists them into a Chroma DB under `chroma/`

### How it works
1. Discover files (.pdf, .txt, .docx) under `data/`.
2. Load with format-specific loaders:
   - TXT: TextLoader
   - PDF: PyMuPDFLoader
   - DOCX: Docx2txtLoader
3. Split with RecursiveCharacterTextSplitter.
4. Embed with HuggingFaceEmbeddings (MiniLM) and persist via Chroma.

### Run
```bash
python scripts/create_database.py
```

### Configuration
Edit `scripts/create_database.py`:
- CHUNK_SIZE / CHUNK_OVERLAP: controls retrieval granularity
- SUPPORTED_EXTENSIONS: add/remove formats
- Embedding model: update the HuggingFaceEmbeddings model_name

### Supported formats
- PDF (.pdf)
- Plain text (.txt)
- Word documents (.docx)

### Notes
- Running the script clears and rebuilds the `chroma/` directory.
- Ensure dependencies are installed: PyMuPDF, docx2txt.
- Large documents (like the included "Moby Dick (The Whale)") are ideal for testing long-context retrieval.
