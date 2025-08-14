import os
import shutil
from langchain.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from app.config import DATA_DIR, CHROMA_DIR


DATA_PATH = DATA_DIR / "books" / "moby_dick_the_whale.txt"


def main():
    generate_data_store()


def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)


def load_documents():
    # Loads txt data
    loader = TextLoader(str(DATA_PATH))
    documents = loader.load_and_split()
    return documents


def split_text(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=100,
        length_function=len,
        add_start_index=True,
    )
    chunks = text_splitter.split_documents(documents)

    print("___________")
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    print("___________")

    document = chunks[50]
    print(document.page_content)
    print(document.metadata)

    return chunks


def save_to_chroma(chunks: list[Document]):
    if os.path.exists(CHROMA_DIR):
        shutil.rmtree(CHROMA_DIR)

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR),
    )
    db.persist()
    print(f"Saved {len(chunks)} chunks to {CHROMA_DIR}.")


if __name__ == "__main__":
    main()





