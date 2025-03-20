# src/blog_generator/graph/nodes/generate_code.py
from src.blog_generator.LLMs.models import get_groq_llm
from src.blog_generator.vectorstore.vector_db import create_vector_store, retrieve_relevant_docs

def generate_code(state):
    llm = get_groq_llm()
    topic = state.get("user_inputs").get("topic")
    vector_store = create_vector_store()
    relevant_docs = retrieve_relevant_docs(vector_store, topic)
    context = "\n".join([doc.page_content for doc in relevant_docs])
    prompt = f"Generate code for a blog post about {topic} based on the context:\n{context}"
    response = llm.invoke(prompt)
    state.update({"code": response.content})
    return state