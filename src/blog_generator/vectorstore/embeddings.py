# src/blog_generator/vectorstore/embeddings.py
# src/blog_generator/vectorstore/embeddings.py
from sentence_transformers import SentenceTransformer

def get_embeddings():
    """Returns an instance of the SentenceTransformer model."""
    return SentenceTransformer('all-mpnet-base-v2') # or other model.