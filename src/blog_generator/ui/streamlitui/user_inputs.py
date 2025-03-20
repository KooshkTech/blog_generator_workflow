# src/blog_generator/ui/streamlitui/user_inputs.py
import streamlit as st

def get_user_inputs():
    topic = st.text_input("Enter blog topic:")
    target_audience = st.text_input("Enter target audience:")
    return {"topic": topic, "target_audience": target_audience}