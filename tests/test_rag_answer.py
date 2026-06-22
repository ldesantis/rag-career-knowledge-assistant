from app.services.rag_service import generate_rag_answer
from app.services.vector_store_service import (
    get_collection,
    store_chunks
)


def test_generate_rag_answer():
    collection = get_collection()

    existing_ids = collection.get()["ids"]

    if existing_ids:
        collection.delete(ids=existing_ids)

    embedded_chunks = [
        {
            "source": "resume.txt",
            "chunk_id": 1,
            "content": "Louis has experience with machine learning and AI engineering.",
            "embedding": [0.1] * 384
        }
    ]

    store_chunks(embedded_chunks)

    answer = generate_rag_answer(
        question="What AI experience does Louis have?",
        top_k=1
    )

    print(answer)

    assert "machine learning" in answer.lower() or "ai engineering" in answer.lower()