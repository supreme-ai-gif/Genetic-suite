import os
from openai import OpenAI

def ai_generate(tool, text):
    try:
        api_key = os.environ.get("OPENAI_API_KEY")

        if not api_key:
            return "❌ AI is not configured. API key missing."

        if not text.strip():
            return "Please enter some text."

        client = OpenAI(api_key=api_key)

        if tool == "writer":
            prompt = f"Write a detailed, high-quality essay about:\n{text}"

        elif tool == "rewriter":
            prompt = f"Rewrite the following text professionally:\n{text}"

        elif tool == "summarizer":
            prompt = f"Summarize the following text clearly and concisely:\n{text}"

        else:
            return "Unknown tool."

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a professional AI writing assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=800
        )

        return response.choices[0].message.content

    except Exception as e:
        # IMPORTANT: Never crash Flask
        return f"⚠️ AI Error: {str(e)}"
