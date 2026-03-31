import streamlit as st
from pathlib import Path
import streamlit.components.v1 as components

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
        [data-testid="stAppViewContainer"] {padding: 0; overflow: hidden;}
        [data-testid="stHeader"] {display: none;}
        [data-testid="stBottom"] {display: none;}
        iframe {border: none;}
        [data-testid="stVerticalBlockBorderWrapper"] {padding: 0 !important;}
        [data-testid="element-container"] {padding: 0 !important; margin: 0 !important;}
        .element-container iframe {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            z-index: 999 !important;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "index.html"
html_content = html_path.read_text(encoding="utf-8")

components.html(html_content, height=900, scrolling=True)
