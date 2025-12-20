def ai_generate(tool, text):
    text = text.strip()

    if not text:
        return "Please enter some text."

    if tool == "writer":
        return (
            "📝 Generated Essay:\n\n"
            + text
            + "\n\n(This is a sample AI-written response.)"
        )

    elif tool == "rewriter":
        return (
            "🔁 Rewritten Version:\n\n"
            + text.replace(" very ", " extremely ")
            .replace(" good ", " excellent ")
            .replace(" bad ", " poor ")
        )

    elif tool == "summarizer":
        return (
            "📌 Summary:\n\n"
            + (text[:150] + "..." if len(text) > 150 else text)
        )

    return "Unknown tool selected."
