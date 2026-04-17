import ollama

def answer_question(question, context):
    prompt = f"""
You are a precise AI assistant.

Use ONLY the provided context.
If answer is not found, say: "Answer not found in the context."

Context:
{context}

Question:
{question}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']