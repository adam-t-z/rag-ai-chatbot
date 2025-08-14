import os
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

from app.config import CHROMA_DIR

PROMPT_TEMPLATE = """
Answer the question based only on the following context:
Make your answer be a paragraph or a sentence.
{context}

---

Answer the question based on the above context: {question}
"""


class QueryEngine:
    def __init__(self):
        print("[INIT] Loading embeddings and Chroma DB...")
        self.embedding_function = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        self.db = Chroma(
            persist_directory=str(CHROMA_DIR),
            embedding_function=self.embedding_function,
        )
        print("[INIT] Done.")

        self.prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)

        self.openrouter_api_key = os.getenv("OPENROUTER_API_KEY")
        self.chat_model = ChatOpenAI(
            openai_api_key=self.openrouter_api_key,
            model_name="deepseek/deepseek-r1-0528:free",
            openai_api_base="https://openrouter.ai/api/v1",
        )

    def query(self, question: str) -> dict:
        print(f"[QUERY] Searching for: {question}")
        results = self.db.similarity_search_with_relevance_scores(question, k=3)

        if not results:
            return {"answer": "No relevant context found.", "sources": []}

        context_text = "\n\n---\n\n".join([doc.page_content for doc, _ in results])
        prompt = self.prompt_template.format(context=context_text, question=question)
        response = self.chat_model.invoke([HumanMessage(content=prompt)])
        sources = [doc.page_content for doc, _ in results]
        return {"answer": response.content, "sources": sources}





