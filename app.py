import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="O-Health Band",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Hide Streamlit default UI elements for a clean full-page look
st.markdown(
    """
    <style>
        #MainMenu {visibility: hidden;}
        header {visibility: hidden;}
        footer {visibility: hidden;}
        .stApp {background: rgb(15, 16, 20);}
        .block-container {padding: 0 !important; max-width: 100% !important;}
        [data-testid="stAppViewContainer"] {padding: 0;}
        [data-testid="stHeader"] {display: none;}
        iframe {border: none;}
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "index.html"
html_content = html_path.read_text(encoding="utf-8")

st.components.v1.html(html_content, height=700, scrolling=False)
