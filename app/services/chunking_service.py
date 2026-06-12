def chunk_documents(documents: list[dict], chunk_size: int = 500) -> list[dict]:
    chunks = []

    for document in documents:
        source = document["source"]
        content = document["content"]

        for start_index in range(0, len(content), chunk_size):
            chunk_text = content[start_index:start_index + chunk_size]

            chunks.append({
                "source": source,
                "chunk_id": len(chunks) + 1,
                "content": chunk_text
            })

    return chunks