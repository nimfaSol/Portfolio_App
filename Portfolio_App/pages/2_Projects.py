import streamlit as st
import json
import os

st.title("💻 Projects")

# Get the data file path
script_dir = os.path.dirname(os.path.abspath(__file__))
project_dir = os.path.dirname(script_dir)
data_file = os.path.join(project_dir, "data", "projects.json")

with open(data_file) as f:
    projects = json.load(f)

cols = st.columns(2)

for i, proj in enumerate(projects):
    with cols[i % 2]:
        st.markdown(f"""
        <div class="card">
        <h3>{proj['title']}</h3>
        <p>{proj['description']}</p>
        {"".join([f"<span class='tech'>{t}</span>" for t in proj['tech']])}
        <br><br>
        <a href="{proj['link']}" target="_blank">🔗 View Project</a>
        </div>
        """, unsafe_allow_html=True)