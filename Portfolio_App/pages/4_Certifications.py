import streamlit as st
import os
from PIL import Image

st.title("📄 Received Certifications")

# Get the assets directory
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
assets_dir = os.path.join(project_dir, "assets")

# Adding a single certification image
try:
    cert2 = Image.open(os.path.join(assets_dir, "Cert2.png"))
    st.image(cert2, caption="Machine Learning Specialization - 2026")
    
    cert1 = Image.open(os.path.join(assets_dir, "cert1.png"))
    st.image(cert1, caption="Python Specialization - 2026")
    
    cert3 = Image.open(os.path.join(assets_dir, "Cert3.png"))
    st.image(cert3, caption="JavaScript Specialization - 2026")
except FileNotFoundError as e:
    st.error(f"Certificate image not found: {e}")