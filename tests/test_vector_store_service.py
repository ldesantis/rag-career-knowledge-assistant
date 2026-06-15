from app.services.vector_store_service import get_collection


def test_get_collection_creates_collection():
    collection = get_collection()

    assert collection is not None
    assert collection.name == "career_knowledge"