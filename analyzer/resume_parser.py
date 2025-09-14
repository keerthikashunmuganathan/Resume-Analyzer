from PyPDF2 import PdfReader
import docx

def extract_text(file):
    text = ""
    if file.name.endswith('.pdf'):
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            if page.extract_text():
                text += page.extract_text() + " "
    elif file.name.endswith('.docx'):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + " "
    else:
        raise ValueError("Unsupported file format. Use PDF or DOCX")

    return text.strip()
