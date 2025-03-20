# src/blog_generator/ui/streamlitui/test_cases_review.py
import streamlit as st
from src.blog_generator.tools.utils import approve_or_reject

def review_test_cases(test_cases):
    st.write("## Test Cases Review")
    for case in test_cases:
        st.write("- ", case)
    approval = st.text_input("Approve or Reject?")
    return approve_or_reject(approval)