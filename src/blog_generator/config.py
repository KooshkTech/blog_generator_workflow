# src/blog_generator/config.py
import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

VECTOR_STORE_PATH = "vector_db"
VECTOR_STORE_DATA = [
    "Document 1: AI in healthcare is transforming...",
    "Document 2: Benefits of AI in medicine...",
    "Design Document 1: Structure...",
    "Design Document 2: User Interface...",
    "Code Snippet 1: Function to generate...",
    "Code Snippet 2: Class for data handling...",
    "Test Case 1: Verify correct output...",
    "Test Case 2: Check for edge cases...",
]

UI_THEME = {
    "primaryColor": "#4CAF50",  # Keep primary color as is for buttons
    "backgroundColor": "#000000",  # Black background
    "secondaryBackgroundColor": "#1E1E1E",  # Darker background for elements
    "textColor": "#FFFFFF",  # White text
    "font": "sans serif",
}

UI_LAYOUT = {
    "wideMode": True,
}