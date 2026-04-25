import streamlit as st
import os

st.title("📄 Received Certifications")

# Get the assets directory
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
assets_dir = os.path.join(project_dir, "assets")

# Adding a single certification image
st.image(os.path.join(assets_dir, "Cert2.png"), caption="Machine Learning Specialization - 2026")
st.image(os.path.join(assets_dir, "Cert1.png"), caption="Python Specialization - 2026")
st.image(os.path.join(assets_dir, "Cert3.png"), caption="JavaScript Specialization - 2026")