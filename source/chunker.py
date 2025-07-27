import os

def chunk_text(text, chunk_size=3):
    # Split using Bengali Danda symbol '।'
    sentences = text.split('।')
    # Clean and remove empty
    sentences = [s.strip() for s in sentences if s.strip()]
    # Re-add '।' at the end of each sentence
    sentences = [s + '।' for s in sentences]
    # Group into chunks
    chunks = [' '.join(sentences[i:i + chunk_size]) for i in range(0, len(sentences), chunk_size)]
    return chunks

if __name__ == "__main__":
    input_file = "data/cleaned_text.txt"
    output_file = "data/chunks.txt"

    if not os.path.exists(input_file):
        print(f"File not found: {input_file}")
        exit()

    with open(input_file, "r", encoding="utf-8") as f:
        text = f.read()

    chunks = chunk_text(text)

    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(chunk + "\n\n")

    print(f"Chunking complete! {len(chunks)} chunks written to {output_file}.")
