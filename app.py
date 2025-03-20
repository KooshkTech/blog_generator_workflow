# app.py (updated)
import streamlit as st
from src.blog_generator.graph.graph import create_graph
from src.blog_generator.ui.streamlitui import user_inputs, product_owner, design_review, code_review, security_review, test_cases_review, qa_testing, display_result
from src.blog_generator.config import UI_THEME, UI_LAYOUT

# Set up Streamlit page
st.set_page_config(
    page_title="Blog Generator Workflow",
    layout="wide" if UI_LAYOUT["wideMode"] else "centered",
)

# Apply UI theme
st.markdown(
    f"""
    <style>
    body {{
        color: {UI_THEME['textColor']};
        background-color: {UI_THEME['backgroundColor']};
        font-family: {UI_THEME['font']};
    }}
    .stApp {{
        background-color: {UI_THEME['backgroundColor']};
    }}
    .css-10trblm {{
        background-color: {UI_THEME['secondaryBackgroundColor']};
    }}
    .stButton>button {{
        background-color: {UI_THEME['primaryColor']};
        color: white;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("Blog Generator Workflow")

# Get user inputs
user_data = user_inputs.get_user_inputs()

if st.button("Start Workflow"):
    graph = create_graph()
    inputs = {"user_inputs": user_data}
    results = {}

    # Run the workflow using `stream`
    for output in graph.stream(inputs):
        for key, value in output.items():
            results.update(value)

    # UI Interactions for Reviews
    if "user_stories" in results:
        results["user_stories_approved"] = product_owner.review_user_stories(results["user_stories"])
    if "design_documents" in results:
        results["design_approved"] = design_review.review_design_documents(results["design_documents"])
    if "code" in results:
        results["code_approved"] = code_review.review_code(results["code"])
        results["security_approved"] = security_review.review_security(results["code"])
    if "test_cases" in results:
        results["test_cases_approved"] = test_cases_review.review_test_cases(results["test_cases"])
    if "qa_results" not in results:
        results["qa_results"] = qa_testing.qa_results()

    # Display results
    display_result.display_results(results)