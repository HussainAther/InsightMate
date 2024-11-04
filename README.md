# InsightMate

InsightMate is a retrieval-augmented generation (RAG) application built to streamline tech support workflows. It combines NVIDIA’s NeMo Retriever, Guardrails, and NIM Microservices with LlamaIndex to create an intelligent, responsive chatbot that retrieves and summarizes technical documentation, helping support teams address customer queries accurately and efficiently.

## Features

- **Efficient Information Retrieval**: Uses NeMo Retriever to fetch relevant documents and technical information.
- **Enhanced Safety and Reliability**: NeMo Guardrails ensures responses are on-topic, safe, and aligned with support standards.
- **Seamless Inference Management**: Powered by NIM Microservices for efficient query processing and response generation.

## File Overview

- **src/inference_manager.py**: Manages API calls to NVIDIA NIM microservices, coordinating data flow for inference tasks.
- **src/document_retriever.py**: Implements NeMo Retriever to fetch relevant knowledge base content based on user queries.
- **src/response_guardrails.py**: Uses NeMo Guardrails to validate and filter responses, ensuring safe and relevant outputs.
- **src/utils/config.py**: Contains configuration settings for NVIDIA and LlamaIndex integrations.
- **docs/setup_guide.md**: Step-by-step guide for setting up the development environment and configuring dependencies.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/HussainAther/InsightMate.git
   cd InsightMate

