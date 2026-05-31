from app.services.document_loader import load_text_documents


def test_load_text_documents_returns_documents():
    documents = load_text_documents("data/documents")

    assert len(documents) == 3
    assert documents[0]["source"] == "ai_project_notes.txt"
    assert documents[1]["source"] == "job_posting.txt"
    assert documents[2]["source"] == "resume.txt"


def test_loaded_documents_have_content():
    documents = load_text_documents("data/documents")

    for document in documents:
        assert "source" in document
        assert "content" in document
        assert document["content"].strip() != ""