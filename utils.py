def ai_generate(tool, text):
    if not text.strip():
        return "Please enter some text."

    if tool == 'writer':
        return f"📝 Generated Essay:\n\n{text}\n\n(Professional AI output)"

    if tool == 'rewriter':
        return "🔁 Rewritten Text:\n\n" + text.replace(" very ", " extremely ")

    if tool == 'summarizer':
        return "📌 Summary:\n\n" + (text[:150] + '...' if len(text) > 150 else text)

    return "Unknown tool"
