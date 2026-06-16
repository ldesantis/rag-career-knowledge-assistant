import chromadb


COLLECTION_NAME = "career_knowledge"


def get_chroma_client():
    return chromadb.PersistentClient(path="data/chroma")


def get_collection():
    client = get_chroma_client()

    return client.get_or_create_collection(
        name=COLLECTION_NAME
    )


def store_chunks(embedded_chunks: list[dict]) -> None:
    collection = get_collection()

    ids = []
    documents = []
    embeddings = []
    metadatas = []

    for chunk in embedded_chunks:
        ids.append(f"{chunk['source']}_{chunk['chunk_id']}")
        documents.append(chunk["content"])
        embeddings.append(chunk["embedding"])
        metadatas.append({
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"]
        })

    collection.add(
        ids=ids,
        documents=documents,
        embeddings=embeddings,
        metadatas=metadatas
    )

def search_chunks(query_embedding: list[float], top_k: int = 3) -> list[dict]:
    collection = get_collection()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    retrieved_chunks = []

    for index in range(len(results["ids"][0])):
        retrieved_chunks.append({
            "id": results["ids"][0][index],
            "content": results["documents"][0][index],
            "metadata": results["metadatas"][0][index],
            "distance": results["distances"][0][index]
        })

    return retrieved_chunks