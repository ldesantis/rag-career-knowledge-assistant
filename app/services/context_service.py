def build_context(retrieved_chunks: list[dict]) -> str:
    context_parts = []

    for chunk in retrieved_chunks:
        source = chunk["metadata"]["source"]
        chunk_id = chunk["metadata"]["chunk_id"]
        content = chunk["content"]

        context_parts.append(
            f"Source: {source} | Chunk: {chunk_id}\n{content}"
        )

    return "\n\n---\n\n".join(context_parts)