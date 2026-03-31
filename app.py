import streamlit as st
from pathlib import Path
import base64

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
    </style>
    """,
    unsafe_allow_html=True,
)

html_path = Path(__file__).parent / "index.html"
html_content = html_path.read_text(encoding="utf-8")

# Encode HTML as base64 data URI to avoid Streamlit component size limits
html_b64 = base64.b64encode(html_content.encode("utf-8")).decode("utf-8")

st.markdown(
    f'<iframe src="data:text/html;base64,{html_b64}" '
    f'style="width:100%;height:100vh;border:none;position:fixed;top:0;left:0;z-index:999;" '
    f'allowfullscreen></iframe>',
    unsafe_allow_html=True,
)
