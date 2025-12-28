import os
import requests

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"

def ai_generate(tool, text):
    if not text or not text.strip():
        return "⚠️ Please enter some text."

    if not OPENROUTER_API_KEY:
        return "⚠️ AI not configured. Missing OpenRouter API key."

    # Prompt selection
    if tool == "writer":
        prompt = f"Write a detailed, professional essay on the following topic:\n{text}"
    elif tool == "rewriter":
        prompt = f"Rewrite the following text clearly and professionally:\n{text}"
    elif tool == "summarizer":
        prompt = f"Summarize the following text in a clear and concise way:\n{text}"
    else:
        return "⚠️ Unknown AI tool."

    payload = {
        "model": "mistralai/mistral-7b-instruct",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 600,
        "temperature": 0.7
    }

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            OPENROUTER_URL,
            headers=headers,
            json=payload,
            timeout=30
        )
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        return f"⚠️ AI Error: {str(e)}"
    except KeyError:
        return "⚠️ AI Error: Unexpected response format"
