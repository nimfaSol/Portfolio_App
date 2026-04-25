import streamlit as st
from PIL import Image
import os

# Get the directory where this script is located, then go up and into assets
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
assets_dir = os.path.join(project_dir, "assets")

col1, col2 = st.columns([1,2])

with col1:
    try:
        profile_img = Image.open(os.path.join(assets_dir, "nymf.png"))
        st.image(profile_img, width=250)
    except FileNotFoundError:
        st.error("Profile image not found")

with col2:
    st.title("👨‍💻  I'm Nimfa Mae A. Solasco, an aspiring  Machine learning Engineer  ")
    st.subheader("Software Engineer | Machine learning")

    st.markdown("""
    <div class="card">
    Designing & Developing ML Systems
Architecting scalable, end-to-end pipelines that bridge the gap between experimental models and production-ready software.
I aso build scalable systems, simulations, and modern web apps.
    Skills focused on:
    
-Pipeline Engineering: Building modular workflows for data ingestion, cleaning, and feature engineering.

-System Optimization: Tuning high-performance algorithms for speed, accuracy, and resource efficiency.

-Production Integration: Deploying robust ML architectures into functional, responsive application environments.
    </div>
    """, unsafe_allow_html=True)

st.markdown("## ⚡ Tech Stack")
st.code("PyTorch | Scikit-learn | TensorFlow | JavaScript | SQL | Plotly", language="bash")