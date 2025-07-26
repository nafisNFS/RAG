

import fitz 

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    full_text = ""

    for page in doc:
        text = page.get_text()
        full_text += text + "\n"

    doc.close()
    return full_text

if __name__ == "__main__":
    pdf_path = "E:/RAG/HSC26-Bangla1st-Paper.pdf"
    raw_text = extract_text_from_pdf(pdf_path)

    with open("data/raw_text.txt", "w", encoding="utf-8") as f:
        f.write(raw_text)

    print("Text extraction complete.")
