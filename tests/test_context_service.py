from app.services.context_service import build_context


def test_build_context():
    retrieved_chunks = [
        {
            "content": "Machine learning engineer",
            "metadata": {
                "source": "resume.txt",
                "chunk_id": 1
            }
        }
    ]

    context = build_context(retrieved_chunks)

    assert "resume.txt" in context
    assert "Machine learning engineer" in context