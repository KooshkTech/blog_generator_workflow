from langchain_groq import ChatGroq
from src.blog_generator.config import GROQ_API_KEY

def get_groq_llm():
    return ChatGroq(api_key=GROQ_API_KEY, model_name="mixtral-8x7b-32768")