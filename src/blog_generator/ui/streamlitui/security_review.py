# src/blog_generator/ui/streamlitui/security_review.py
import streamlit as st
from src.blog_generator.tools.utils import approve_or_reject

def review_security(code):
    st.write("## Security Review")
    st.write("Simulating security review for:\n", code)
    approval = st.text_input("Approve or Reject?")
    return approve_or_reject(approval)