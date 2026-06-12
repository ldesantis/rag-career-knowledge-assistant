from app.services.chunking_service import chunk_documents


def test_chunk_documents_creates_chunks():
    documents = [
        {
            "source": "test.txt",
            "content": "ABCDEFGHIJKL"
        }
    ]

    chunks = chunk_documents(documents, chunk_size=5)

    assert len(chunks) == 3

    assert chunks[0]["content"] == "ABCDE"
    assert chunks[1]["content"] == "FGHIJ"
    assert chunks[2]["content"] == "KL"


def test_chunks_preserve_source_metadata():
    documents = [
        {
            "source": "resume.txt",
            "content": "ABCDEFGHIJKL"
        }
    ]

    chunks = chunk_documents(documents, chunk_size=5)

    for chunk in chunks:
        assert chunk["source"] == "resume.txt"