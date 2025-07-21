import streamlit as st
import pickle
import PyPDF2
import docx
import spacy

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load pickled model and vectorizer
clf = pickle.load(open("clf.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

# Mapping of prediction id to job category
category_mapping = {
    15: "Java Developer",
    23: "Testing",
    8: "DevOps Engineer",
    20: "Python Developer",
    24: "Web Designing",
    12: "HR",
    3: "Hadoop",
    18: "Blockchain",
    10: "ETL Developer",
    13: "Operations Manager",
    6: "Data Science",
    22: "Sales",
    16: "Mechanical Engineer",
    1: "Arts",
    7: "Database",
    11: "Electrical Engineering",
    14: "Health and fitness",
    19: "PMO",
    4: "Business Analyst",
    9: "DotNet Developer",
    2: "Automation Testing",
    17: "Network Security Engineer",
    21: "SAP Developer",
    5: "Civil Engineer",
    0: "Advocate"
}

# Clean resume text
def clean_resume_spacy(resume_text):
    doc = nlp(resume_text.lower())
    cleaned = ' '.join([token.lemma_ for token in doc if not token.is_stop and token.is_alpha])
    return cleaned

# Extract text from file
def extract_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(uploaded_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    elif uploaded_file.name.endswith(".docx"):
        doc = docx.Document(uploaded_file)
        return "\n".join([para.text for para in doc.paragraphs])
    else:
        return None

# Streamlit UI
def main():
    st.title("📄 Resume Screening App")
    st.write("Upload a resume (PDF or DOCX) and predict the job category.")

    uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

    if uploaded_file:
        raw_text = extract_text_from_file(uploaded_file)
        if raw_text:
            st.subheader("📜 Extracted Text Preview:")
            st.write(raw_text[:500] + "...")

            cleaned = clean_resume_spacy(raw_text)
            input_vector = tfidf.transform([cleaned])
            prediction_id = clf.predict(input_vector)[0]
            category_name = category_mapping.get(prediction_id, "Unknown")

            st.success(f"✅ **Predicted Job Category**: {category_name}")
        else:
            st.error("❌ Could not extract text from the uploaded file.")




if __name__ == "__main__":
    main()
