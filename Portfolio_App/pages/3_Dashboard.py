import streamlit as st
import plotly.express as px
import pandas as pd

st.title("📊 Analytics Dashboard")

data = {
    "Project": ["CPU Sim", "SK System", "ATM System"],
    "Complexity": [8, 7, 6],
    "Impact": [9, 8, 7]
}

df = pd.DataFrame(data)

fig = px.bar(df, x="Project", y="Impact", title="Project Impact")
st.plotly_chart(fig, use_container_width=True)