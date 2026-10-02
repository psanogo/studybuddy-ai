import streamlit as st

st.set_page_config(page_title="StudyBuddy AI")

st.title("🎓 StudyBuddy AI")
st.subheader("AI-Powered Study Assistant")

uploaded_file = st.file_uploader(
    "Upload PDF or TXT notes",
    type=["pdf", "txt"]
)

if uploaded_file:
    st.success(f"Uploaded: {uploaded_file.name}")

    if st.button("Generate Summary"):
        st.info("AI summary feature coming next!")

    if st.button("Generate Quiz"):
        st.info("AI quiz feature coming next!")

    if st.button("Create Study Plan"):
        st.info("Study planner feature coming next!")
