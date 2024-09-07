pdf_path = "./Anayasa.pdf"

from PyPDF2 import PdfReader
# pip install PyPDF2

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as file:
        pdf = PdfReader(file)
        text = ""
        for page_num in range(len(pdf.pages)):
            page = pdf.pages[page_num]
            text += page.extract_text()
    return text

text = extract_text_from_pdf(pdf_path)
lines = text.split("\n")
# remove empty lines and lines with only whitespace
lines = [line for line in lines if line.strip()]
print(lines[:100])
