# resume-parser-app
# AI Resume Analyzer 🧠📄

A simple NLP-powered Streamlit app that extracts key information (name, email, phone, skills, etc.) from resumes and recommends suitable job roles.

🚀 Live Demo on Hugging Face → [Click here to try it out!](https://huggingface.co/spaces/Shahwar/resume-parser)

---

## 📄 Features

- 📂 Upload PDF or DOCX resumes
- 🧠 Named Entity Recognition using spaCy
- 📧 Extracts name, email, phone number
- 💡 Identifies key skills from the text
- 🧑‍💻 Suggests relevant job roles (ML Engineer, Data Analyst, etc.)
- 💾 Download extracted text

---

## 🛠️ Tech Stack

- Python
- Streamlit
- spaCy
- pdfplumber
- docx2txt

---

## 📦 Installation (for local use)

```bash
git clone https://github.com/YOUR-USERNAME/resume-analyzer.git
cd resume-analyzer
pip install -r requirements.txt
python -m spacy download en_core_web_sm
streamlit run app.py










