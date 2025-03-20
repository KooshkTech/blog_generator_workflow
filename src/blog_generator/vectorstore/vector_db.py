# src/blog_generator/vectorstore/vector_db.py
from langchain_community.vectorstores import FAISS
from src.blog_generator.vectorstore.embeddings import get_embeddings
from src.blog_generator.config import VECTOR_STORE_DATA
from langchain_core.documents import Document

def create_vector_store(texts=VECTOR_STORE_DATA):
    """Creates a FAISS vector store from a list of texts."""
    embeddings_model = get_embeddings()
    documents = [Document(page_content=t) for t in texts]
    vector_store = FAISS.from_documents(documents, embeddings_model)
    return vector_store

def retrieve_relevant_docs(vector_store, query, k=4):
    """Retrieves relevant documents from the vector store."""
    relevant_docs = vector_store.similarity_search(query, k=k)
    return relevant_docs