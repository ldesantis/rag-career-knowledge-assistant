from app.services.vector_store_service import (
    get_collection,
    store_chunks
)


def test_store_chunks():
    collection = get_collection()

    existing_ids = collection.get()["ids"]

    if existing_ids:
        collection.delete(ids=existing_ids)

    embedded_chunks = [
        {
            "source": "test.txt",
            "chunk_id": 1,
            "content": "Machine learning engineer",
            "embedding": [0.1] * 384
        }
    ]

    store_chunks(embedded_chunks)

    results = collection.get()

    assert len(results["ids"]) == 1