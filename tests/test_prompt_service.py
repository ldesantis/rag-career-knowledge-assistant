from app.services.prompt_service import build_prompt


def test_build_prompt():
    question = "What is machine learning?"

    context = """
Source: notes.txt | Chunk: 1
Machine learning is a branch of AI.
"""

    prompt = build_prompt(question, context)

    assert "What is machine learning?" in prompt
    assert "Machine learning is a branch of AI." in prompt
    assert "I don't know based on the provided context." in prompt