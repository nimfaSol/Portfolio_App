import streamlit as st
import os

st.set_page_config(
    page_title="Dev Portfolio",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load global CSS
def load_css():
    css_path = os.path.join(os.path.dirname(__file__), "assets", "styles.css")
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# Custom Navbar
st.markdown("""
<div class="nav">
    <h2>🚀 DevPortfolio</h2>
</div>
""", unsafe_allow_html=True)