from sentence_transformers import SentenceTransformer


MODEL_NAME = "all-MiniLM-L6-v2"


def load_embedding_model():
    return SentenceTransformer(MODEL_NAME)


def embed_chunks(chunks: list[dict]) -> list[dict]:
    model = load_embedding_model()

    embedded_chunks = []

    for chunk in chunks:
        embedding = model.encode(chunk["content"])

        embedded_chunks.append({
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"],
            "content": chunk["content"],
            "embedding": embedding.tolist()
        })

    return embedded_chunks