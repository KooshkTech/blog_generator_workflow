# src/blog_generator/tools/utils.py
def approve_or_reject(input_text):
    """Simulates approval or rejection based on input."""
    if "approve" in input_text.lower():
        return True
    elif "reject" in input_text.lower():
        return False
    else:
        return None