import streamlit as st
import docx2txt
import pdfplumber
import io
import spacy
import re
import os
import subprocess

# Ensure the spaCy model is installed
spacy_model = "en_core_web_sm"
try:
    nlp = spacy.load(spacy_model)
except OSError:
    st.warning(f"Downloading {spacy_model} model... Please wait.")
    subprocess.run(["python", "-m", "spacy", "download", spacy_model])
    nlp = spacy.load(spacy_model)

st.title("📝 AI Resume Analyzer")

# Upload resume
uploaded_file = st.file_uploader("Upload Your Resume", type=["pdf", "docx"])

if uploaded_file is not None:
    st.success(f"Uploaded: {uploaded_file.name}")

    def extract_text(file):
        if file.type == "application/pdf":
            with pdfplumber.open(file) as pdf:
                text = "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
        elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            text = docx2txt.process(file)
        else:
            text = "Unsupported file format"
        return text

    # Extract text from resume
    resume_text = extract_text(uploaded_file)
    st.subheader("📜 Extracted Resume Text:")
    st.text_area("Resume Content", resume_text, height=250)

    # NLP Processing
    doc = nlp(resume_text)

    # Extract Name
    name = next((ent.text for ent in doc.ents if ent.label_ == "PERSON"), "Not Found")
    st.write(f"**🧑 Candidate Name:** {name}")

    # Extract Email
    email = re.findall(r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+", resume_text)
    st.write(f"**📧 Email:** {email[0] if email else 'Not Found'}")

    # Extract Phone Number
    phone = re.findall(r"\+?\d{10,13}", resume_text)
    st.write(f"**📞 Phone Number:** {phone[0] if phone else 'Not Found'}")

    # Extract Skills
    skills = ["Python", "SQL", "Machine Learning", "Data Analysis", "NLP", "Tableau", "Excel"]
    extracted_skills = [skill for skill in skills if skill.lower() in resume_text.lower()]
    st.write(f"**💡 Skills Identified:** {', '.join(extracted_skills) if extracted_skills else 'No Matching Skills Found'}")

    # Recommended Job Roles
    if "machine learning" in resume_text.lower():
        st.write("✅ **Recommended Job Role:** Machine Learning Engineer")
    elif "data analysis" in resume_text.lower():
        st.write("✅ **Recommended Job Role:** Data Analyst")
    elif "nlp" in resume_text.lower():
        st.write("✅ **Recommended Job Role:** NLP Engineer")
    else:
        st.write("✅ **Recommended Job Role:** General Data Science")

    # Download extracted text
    text_io = io.StringIO(resume_text)
    st.download_button(label="📥 Download Extracted Text", data=text_io.getvalue(), file_name="resume_text.txt")

