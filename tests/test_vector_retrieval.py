from app.services.vector_store_service import (
    get_collection,
    store_chunks,
    search_chunks
)


def test_search_chunks_returns_results():
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

    results = search_chunks(
        query_embedding=[0.1] * 384,
        top_k=1
    )

    assert len(results) == 1
    assert results[0]["content"] == "Machine learning engineer"