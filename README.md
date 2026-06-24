# RAG Career Knowledge Assistant

The RAG Career Knowledge Assistant is an AI-powered application that answers questions over career-related documents such as resumes, job postings, project notes, and interview preparation materials.

It uses Retrieval-Augmented Generation to retrieve relevant document chunks, send them as context to a language model, and generate grounded responses with source references.

This project is designed as a portfolio-quality AI engineering project demonstrating RAG architecture, embeddings, vector search, API development, clean project structure, testing, and deployment readiness.

## Features

- Document ingestion and loading
- Text chunking for retrieval optimization
- Embedding generation using Sentence Transformers
- Chroma vector database integration
- Semantic similarity search
- Context assembly from retrieved document chunks
- Prompt construction for Retrieval-Augmented Generation (RAG)
- OpenAI GPT integration for answer generation
- Automated testing with pytest
- Environment variable and API key management

## Architecture

The application follows a Retrieval-Augmented Generation (RAG) architecture:

Documents
↓
Document Loader
↓
Chunking Service
↓
Embedding Service
↓
Chroma Vector Database
↓
Semantic Retrieval
↓
Context Assembly
↓
Prompt Construction
↓
OpenAI GPT
↓
Answer Generation

## Technology Stack

### Programming Language
- Python

### AI & Machine Learning
- OpenAI GPT
- Sentence Transformers
- Retrieval-Augmented Generation (RAG)

### Vector Database
- Chroma

### Testing
- pytest

### Environment Management
- python-dotenv

### Version Control
- Git
- GitHub

## Installation

### Clone the Repository

git clone https://github.com/ldesantis/rag-career-knowledge-assistant.git

cd rag-career-knowledge-assistant

### Create a Virtual Environment

python -m venv .venv

### Activate the Virtual Environment

Windows:

.venv\Scripts\Activate.ps1

### Install Dependencies

pip install -r requirements.txt

## Environment Variables

Create a `.env` file in the project root and add:

OPENAI_API_KEY=your_api_key_here

A template file named `.env.example` is included in the repository.
Copy `.env.example` to `.env` and replace the placeholder value with your OpenAI API key.

## Running Tests

Run all tests:

python -m pytest

Run a specific test:

python -m pytest tests/test_rag_answer.py

Current test coverage includes:

- Document loading
- Text chunking
- Embedding generation
- Vector storage
- Semantic retrieval
- Context assembly
- Prompt generation
- End-to-end RAG workflow

## Project Structure

```text
app/
├── services/
│   ├── document_loader.py
│   ├── chunking_service.py
│   ├── embedding_service.py
│   ├── vector_store_service.py
│   ├── context_service.py
│   ├── prompt_service.py
│   ├── llm_service.py
│   └── rag_service.py
│
data/
├── documents/
├── chroma/
│
docs/
│
tests/
├── test_document_loader.py
├── test_chunking_service.py
├── test_embedding_service.py
├── test_vector_storage.py
├── test_vector_retrieval.py
├── test_context_service.py
├── test_prompt_service.py
├── test_rag_service.py
├── test_rag_answer.py
```

## Future Enhancements

- Support additional document formats (PDF, DOCX)
- Add source citations in generated answers
- Implement a REST API interface
- Add a web-based user interface
- Improve retrieval ranking and relevance scoring
- Support multiple vector database providers
- Add conversation memory and chat history
- Containerize the application with Docker
- Deploy to a cloud platform
- Add evaluation metrics for retrieval and answer quality