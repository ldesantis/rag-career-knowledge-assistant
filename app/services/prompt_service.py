def build_prompt(question: str, context: str) -> str:
    return f"""
You are an AI assistant answering questions using only the provided context.

If the answer is not found in the context, say:
"I don't know based on the provided context."

Context:
{context}

Question:
{question}

Answer:
""".strip()