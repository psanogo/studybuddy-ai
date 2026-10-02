import streamlit as st

st.set_page_config(page_title="StudyBuddy AI")

st.title("🎓 StudyBuddy AI")
st.write("Upload your notes and let AI help you study.")

uploaded_file = st.file_uploader(
    "Upload notes",
    type=["pdf", "txt"]
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")
