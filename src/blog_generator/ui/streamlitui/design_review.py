# src/blog_generator/ui/streamlitui/design_review.py
import streamlit as st
from src.blog_generator.tools.utils import approve_or_reject

def review_design_documents(design_documents):
    st.write("## Design Documents Review")
    st.write(design_documents["content"])
    approval = st.text_input("Approve or Reject?")
    return approve_or_reject(approval)