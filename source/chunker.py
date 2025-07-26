

from nltk.tokenize import sent_tokenize
import nltk
nltk.download("punkt")

def chunk_text(text, chunk_size=3):
    sentences = sent_tokenize(text)
    chunks = [' '.join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]
    return chunks

if __name__ == "__main__":
    with open("data/cleaned_text.txt", "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)

    with open("data/chunks.txt", "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(chunk + "\n\n")

    print(f"Generated {len(chunks)} chunks.")
