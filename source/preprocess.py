

import re

def clean_text(text):
    # Remove page numbers or headers if needed
    text = re.sub(r"\n+", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n\s+", "\n", text)

    return text.strip()

if __name__ == "__main__":
    with open("data/raw_text.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()

    cleaned = clean_text(raw_text)

    with open("data/cleaned_text.txt", "w", encoding="utf-8") as f:
        f.write(cleaned)

    print("Text cleaning complete.")
