# src/blog_generator/ui/streamlitui/display_result.py
import streamlit as st

def display_results(results):
    st.write("## Workflow Results")
    for key, value in results.items():
        st.write(f"**{key}:**")
        if isinstance(value, list):
            for item in value:
                st.write(f"- {item}")
        else:
            st.write(value)