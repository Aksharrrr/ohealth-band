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

# Inject a script to force-play videos when they scroll into view
# (browsers may block autoplay inside iframes until the element is visible)
video_fix = """
<script>
(function() {
  function setupVideoAutoplay() {
    var videos = document.querySelectorAll('video');
    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          entry.target.play().catch(function(){});
        }
      });
    }, {threshold: 0.1});
    videos.forEach(function(v) { observer.observe(v); });
    // Also force-play on any scroll
    window.addEventListener('scroll', function() {
      videos.forEach(function(v) {
        var rect = v.getBoundingClientRect();
        if (rect.top < window.innerHeight && rect.bottom > 0 && v.paused) {
          v.play().catch(function(){});
        }
      });
    }, {passive: true});
  }
  // Run setup now and also after gate dismissal (poll for gate hidden)
  setupVideoAutoplay();
  var gateCheck = setInterval(function() {
    var gate = document.getElementById('gate-overlay');
    if (!gate || gate.style.display === 'none' || gate.classList.contains('hidden')) {
      clearInterval(gateCheck);
      // Re-trigger play on all videos after gate is gone
      setTimeout(function() {
        document.querySelectorAll('video').forEach(function(v) {
          v.play().catch(function(){});
        });
      }, 500);
    }
  }, 300);
})();
</script>
"""
html_content = html_content.replace("</body>", video_fix + "</body>")

components.html(html_content, height=900, scrolling=True)
