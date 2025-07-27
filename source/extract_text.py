import pdfplumber
from pathlib import Path

def extract_text_with_plumber(pdf_path):
    full_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            full_text += page.extract_text() + "\n"
    return full_text

if __name__ == "__main__":
    pdf_path = "/pythonProject1/HSC26-Bangla1st-Paper.pdf"
    output_dir = Path("data")
    output_dir.mkdir(parents=True, exist_ok=True)

    try:
        raw_text = extract_text_with_plumber(pdf_path)
        with open(output_dir / "raw_text.txt", "w", encoding="utf-8") as f:
            f.write(raw_text)
        print("Text extracted.")
    except Exception as e:
        print("Error extracting text:", e)
