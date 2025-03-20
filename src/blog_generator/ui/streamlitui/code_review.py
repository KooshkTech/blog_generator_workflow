# src/blog_generator/ui/streamlitui/code_review.py
import streamlit as st
from src.blog_generator.tools.utils import approve_or_reject

def review_code(code):
    st.write("## Code Review")
    st.code(code)
    approval = st.text_input("Approve or Reject?")
    return approve_or_reject(approval)