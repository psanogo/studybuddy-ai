import streamlit as st

st.set_page_config(page_title="StudyBuddy AI")

st.title("🎓 StudyBuddy AI")
st.write("Your AI-powered study assistant")

uploaded_file = st.file_uploader(
    "Upload your notes",
    type=["pdf", "txt"]
)

if uploaded_file:
    st.success("File uploaded successfully!")
