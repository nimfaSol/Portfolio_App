import streamlit as st
import json

st.title("💻 Projects")

with open("data/projects.json") as f:
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