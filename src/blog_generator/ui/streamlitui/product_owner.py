# src/blog_generator/ui/streamlitui/product_owner.py
import streamlit as st
from src.blog_generator.tools.utils import approve_or_reject

def review_user_stories(user_stories):
    st.write("## User Stories Review")
    st.write(user_stories[0])
    approval = st.text_input("Approve or Reject?")
    return approve_or_reject(approval)