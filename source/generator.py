
import openai

openai.api_key = "your-openai-api-key"

def generate_answer(question, context):
    prompt = f"উত্তর দিন নিচের তথ্য ব্যবহার করে:\n\n{context}\n\nপ্রশ্ন: {question}\nউত্তর:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"].strip()

if __name__ == "__main__":
    context = "কল্যাণীর বয়স ছিল ১৫ বছর।"
    question = "বিয়ের সময় কল্যাণীর প্রকৃত বয়স কত ছিল?"
    print(generate_answer(question, context))
