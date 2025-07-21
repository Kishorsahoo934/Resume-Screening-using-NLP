from fpdf import FPDF

# Replace special characters with ASCII-safe versions
def clean_text(text):
    return (
        text.replace("–", "-")
            .replace("•", "*")
    )

# Create a PDF class
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Adv. Ramesh Kr. Mishra", ln=True, align="C")
        self.set_font("Arial", "", 12)
        self.cell(0, 8, "Advocate, Orissa High Court", ln=True, align="C")
        self.cell(0, 8, "Bar Council Reg. No: OHC/1234/2005", ln=True, align="C")
        self.cell(0, 8, "Email: rkmishra.law@gmail.com | Phone: +91-9876543210", ln=True, align="C")
        self.cell(0, 8, "Address: Plot No-15, Bapuji Nagar, Bhubaneswar, Odisha - 751009", ln=True, align="C")
        self.ln(5)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(5)

    def section_title(self, title):
        self.set_font("Arial", "B", 12)
        self.set_text_color(0, 0, 128)
        self.cell(0, 10, title, ln=True)
        self.set_text_color(0, 0, 0)

    def section_body(self, body):
        self.set_font("Arial", "", 11)
        self.multi_cell(0, 8, clean_text(body))
        self.ln()

# Initialize PDF
pdf = PDF()
pdf.add_page()

# Professional Summary
pdf.section_title("Professional Summary")
pdf.section_body(
    "A dedicated and experienced legal practitioner with over 18 years of experience in handling civil, criminal, "
    "corporate, and cyber law matters. Skilled in legal documentation, client consultation, and judicial proceedings. "
    "Available for legal verification, project validation, and mentorship for academic or research-based work with legal aspects."
)

# Education
pdf.section_title("Educational Background")
pdf.section_body(
    "LL.B. - Utkal University, Odisha (2004)\n"
    "B.A. in Political Science - Ravenshaw University, Cuttack (2001)"
)

# Professional Experience
pdf.section_title("Professional Experience")
pdf.section_body(
    "Senior Advocate - Orissa High Court (2005 - Present)\n"
    "- Handled 800+ civil and criminal cases with high success rates.\n"
    "- Provided legal opinions to corporations and startups.\n"
    "- Frequently collaborated on academic and technical projects involving data privacy and legal compliance.\n\n"
    "Legal Advisor (Freelance) (2016 - Present)\n"
    "- Validated academic projects for B.Tech and MBA students.\n"
    "- Consulted on the legal framework for digital platforms, AI systems, and cybersecurity compliance."
)

# Skills
pdf.section_title("Skills")
pdf.section_body(
    "* Civil & Criminal Law\n* Cyber Law and Data Privacy\n* Legal Documentation & Drafting\n"
    "* Client Consultation\n* Legal Research\n* Project Verification & Academic Validation"
)

# Certifications
pdf.section_title("Certifications")
pdf.section_body(
    "* Certificate in Cyber Law - Indian Law Institute, New Delhi\n"
    "* GDPR Compliance Workshop - NALSAR Hyderabad"
)

# Verification
pdf.section_title("Declaration / Verification Statement")
pdf.section_body(
    "I hereby verify that I have reviewed and validated the following project:\n\n"
    "Project Title: [Your Project Title Here]\n"
    "Project Author: [Kishor sahoo]\n"
    "Institution: [Gift]\n"
    "Verification Date: [01/05/2023]\n\n"
    "Signature: ___________________\n"
    "Date: ___________________"
)

# Save the PDF
output_path = "Demo_Advocate_Resume.pdf"
pdf.output(output_path)
print("PDF saved to:", output_path)
