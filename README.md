# 📄 Resume Screening App using NLP

This is a Streamlit-based web application that uses **Natural Language Processing (NLP)** and **Machine Learning** to predict the most suitable job category for a given resume.

### 🔍 Overview

The app allows users to upload resumes in PDF or DOCX format. It then:
- Extracts and cleans the resume text using **spaCy**
- Vectorizes the text using **TF-IDF**
- Predicts the job category using a pre-trained **ML model**
- Displays the predicted job role to the user

---

## 🚀 Features

- 📤 Upload resumes in `.pdf` or `.docx`
- 🧹 Resume cleaning using spaCy (lemmatization, stopword removal)
- 🤖 Job prediction using a trained ML classifier
- 🎯 Supports 25+ job categories

---

## 🛠 Tech Stack

- 🐍 Python
- 🧠 scikit-learn (for ML model)
- 🗂️ spaCy (for NLP preprocessing)
- 📄 PyPDF2 / python-docx (for resume parsing)
- 📊 TF-IDF Vectorizer
- 🌐 Streamlit (for web app)

---

## 💼 Job Categories Supported

- Advocate  
- Java Developer  
- Python Developer  
- Web Designing  
- Data Science  
- Blockchain  
- DevOps Engineer  
- HR  
- Mechanical Engineer  
- Electrical Engineering  
- Civil Engineer  
- DotNet Developer  
- ETL Developer  
- Automation Testing  
- Testing  
- Network Security Engineer  
- Business Analyst  
- Operations Manager  
- Database  
- Sales  
- SAP Developer  
- PMO  
- Health and fitness  
- Arts  
- Hadoop

---

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/Kishorsahoo934/Resume-Screening-using-NLP.git
cd Resume-Screening-using-NLP
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
python -m spacy download en_core_web_sm
