from app.services.rag_service import generate_rag_prompt
from app.services.vector_store_service import (
    get_collection,
    store_chunks
)


def test_generate_rag_prompt():
    collection = get_collection()

    existing_ids = collection.get()["ids"]

    if existing_ids:
        collection.delete(ids=existing_ids)

    embedded_chunks = [
        {
            "source": "resume.txt",
            "chunk_id": 1,
            "content": "Machine learning engineer",
            "embedding": [0.1] * 384
        }
    ]

    store_chunks(embedded_chunks)

    prompt = generate_rag_prompt(
        question="Tell me about machine learning",
        top_k=1
    )

    assert "Machine learning engineer" in prompt
    assert "Tell me about machine learning" in prompt