from pathlib import Path


def load_text_documents(documents_dir: str) -> list[dict]:
    documents_path = Path(documents_dir)

    if not documents_path.exists():
        raise FileNotFoundError(f"Documents directory not found: {documents_dir}")

    documents = []

    for file_path in sorted(documents_path.glob("*.txt")):
        content = file_path.read_text(encoding="utf-8")

        documents.append({
            "source": file_path.name,
            "content": content
        })

    return documents