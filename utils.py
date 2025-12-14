
def ai_generate(tool, text):
    if tool == "writer":
        return "Generated Essay: " + text
    if tool == "summarizer":
        return "Summary: " + text[:120] + "..."
    if tool == "rewriter":
        return "Rewritten: " + text.replace("very", "extremely")
    return "Result: " + text
