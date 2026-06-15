from app.services.embedding_service import load_embedding_model, embed_chunks


def test_embedding_model_loads():
    model = load_embedding_model()

    embedding = model.encode("Machine learning engineer")

    assert embedding is not None
    assert len(embedding) > 0


def test_embed_chunks_adds_embeddings():
    chunks = [
        {
            "source": "test.txt",
            "chunk_id": 1,
            "content": "Machine learning engineer"
        }
    ]

    embedded_chunks = embed_chunks(chunks)

    assert len(embedded_chunks) == 1
    assert embedded_chunks[0]["source"] == "test.txt"
    assert embedded_chunks[0]["chunk_id"] == 1
    assert embedded_chunks[0]["content"] == "Machine learning engineer"
    assert "embedding" in embedded_chunks[0]
    assert len(embedded_chunks[0]["embedding"]) > 0