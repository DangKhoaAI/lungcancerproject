import streamlit as st
from pathlib import Path

def show_introduction():
    """Displays the introduction page with content from a Markdown file."""
    
    # Construct path to the markdown file relative to this script
    intro_path = Path(__file__).parent / "info" / "intro.md"
    
    with open(intro_path, "r", encoding="utf-8") as f:
        md_content = f.read()
    
    st.markdown(md_content, unsafe_allow_html=True)
