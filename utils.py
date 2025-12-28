import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def ai_generate(tool, text):
    if not text.strip():
        return "Please enter some text."

    if tool == "writer":
        prompt = f"Write a detailed essay about: {text}"

    elif tool == "rewriter":
        prompt = f"Rewrite the following text professionally:\n{text}"

    elif tool == "summarizer":
        prompt = f"Summarize the following text clearly:\n{text}"

    else:
        return "Unknown tool."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful AI writing assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
