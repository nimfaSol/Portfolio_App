import streamlit as st

st.title("📬 Contact")

# --- SOCIAL LINKS ---
# You can use Markdown with emojis or icons
st.write("Connect with me on:")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("[🔗 LinkedIn](https://www.linkedin.com/in/nimfa-solasco-b31a76405/)")
with col2:
    st.markdown("[💻 GitHub](https://github.com/nimfaSol)")
with col3:
    st.markdown("[Facebook](https://www.facebook.com/nimfa.mae.solascoe)")

st.divider() # Adds a subtle line between socials and the form

# --- CONTACT FORM ---
with st.form("contact"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    msg = st.text_area("Message")

    if st.form_submit_button("Send"):
        st.success("🚀 Message sent!")