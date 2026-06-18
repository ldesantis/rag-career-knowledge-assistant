from app.services.embedding_service import load_embedding_model
from app.services.vector_store_service import search_chunks
from app.services.context_service import build_context
from app.services.prompt_service import build_prompt


def generate_rag_prompt(question: str, top_k: int = 3) -> str:
    model = load_embedding_model()

    question_embedding = model.encode(question).tolist()

    retrieved_chunks = search_chunks(
        query_embedding=question_embedding,
        top_k=top_k
    )

    context = build_context(retrieved_chunks)

    prompt = build_prompt(
        question=question,
        context=context
    )

    return prompt