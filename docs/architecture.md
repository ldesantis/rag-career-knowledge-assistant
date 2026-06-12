# Architecture Overview

## Project

RAG Career Knowledge Assistant

## Purpose

This application allows users to ask questions over career-related documents such as resumes, job postings, project notes, certifications, and interview preparation materials.

The system uses Retrieval-Augmented Generation to retrieve relevant document chunks and provide grounded answers using a language model.

## MVP Workflow

1. Load source documents from `data/documents`
2. Split documents into smaller chunks
3. Convert chunks into embeddings
4. Store embeddings in Chroma
5. Accept a user question
6. Retrieve relevant chunks from Chroma
7. Build a prompt using the retrieved context
8. Send the prompt to an LLM
9. Return an answer with source references

## Main Components

### Data Layer

Stores source documents and vector database files.

### Retrieval Layer

Loads documents, chunks text, creates embeddings, stores vectors, and retrieves relevant chunks.

### Generation Layer

Builds prompts and generates answers using an LLM.

### API Layer

Receives user requests and returns responses.

### Frontend Layer

Provides a user interface for asking questions and viewing answers.