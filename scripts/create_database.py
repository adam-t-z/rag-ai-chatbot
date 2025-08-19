import os
import shutil
from pathlib import Path
from typing import Iterable

from langchain_community.document_loaders import (
    TextLoader,
    PyMuPDFLoader,
    Docx2txtLoader,
)
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from app.config import DATA_DIR, CHROMA_DIR


# Chunking configuration (tweak here)
CHUNK_SIZE = 300
CHUNK_OVERLAP = 100

# Supported file types
SUPPORTED_EXTENSIONS = {".txt", ".pdf", ".docx"}


def main():
    generate_data_store()


def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)


def discover_source_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if path.is_file() and path.suffix.lower() in SUPPORTED_EXTENSIONS:
            files.append(path)
    return files


def load_documents() -> list[Document]:
    all_documents: list[Document] = []

    source_files = discover_source_files(DATA_DIR)
    if not source_files:
        print(f"[LOAD] No source files found in {DATA_DIR}. Supported: {sorted(SUPPORTED_EXTENSIONS)}")
        return all_documents

    print(f"[LOAD] Found {len(source_files)} source files. Loading...")

    for file_path in source_files:
        suffix = file_path.suffix.lower()
        try:
            if suffix == ".txt":
                loader = TextLoader(str(file_path), autodetect_encoding=True)
            elif suffix == ".pdf":
                loader = PyMuPDFLoader(str(file_path))
            elif suffix == ".docx":
                loader = Docx2txtLoader(str(file_path))
            else:
                continue

            docs = loader.load()
            all_documents.extend(docs)
        except Exception as exc:
            print(f"[LOAD][WARN] Skipping {file_path.name} due to error: {exc}")

    print(f"[LOAD] Loaded {len(all_documents)} documents from {len(source_files)} files.")
    return all_documents


def split_text(documents: list[Document]) -> list[Document]:
    if not documents:
        print("[SPLIT] No documents to split.")
        return []

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)

    print("___________")
    print(f"[SPLIT] Split {len(documents)} documents into {len(chunks)} chunks.")
    print("___________")

    if len(chunks) > 0:
        sample = chunks[min(50, len(chunks) - 1)]
        print(sample.page_content[:500])
        print(sample.metadata)

    return chunks


def save_to_chroma(chunks: list[Document]) -> None:
    if os.path.exists(CHROMA_DIR):
        shutil.rmtree(CHROMA_DIR)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
    )
    db.persist()
    print(f"[SAVE] Saved {len(chunks)} chunks to {CHROMA_DIR}.")


if __name__ == "__main__":
    main()





