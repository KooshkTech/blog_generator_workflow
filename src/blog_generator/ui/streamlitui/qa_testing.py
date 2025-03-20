# src/blog_generator/ui/streamlitui/qa_testing.py
import streamlit as st

def qa_results():
    results = st.text_input("Enter QA results:")
    return results