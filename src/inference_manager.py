# inference_manager.py

from document_retriever import DocumentRetriever
from response_guardrails import ResponseGuardrails

class InferenceManager:
    def __init__(self):
        self.retriever = DocumentRetriever()
        self.guardrails = ResponseGuardrails()

    def generate_response(self, user_query):
        # Step 1: Retrieve relevant documents
        documents = self.retriever.retrieve_documents(user_query)
        
        # Step 2: Generate response from retrieved documents (placeholder logic)
        raw_response = self.summarize_documents(documents)

        # Step 3: Apply guardrails for safe and relevant output
        safe_response = self.guardrails.apply_guardrails(raw_response)
        
        return safe_response

    def summarize_documents(self, documents):
        # Placeholder logic for summarizing documents
        # In a real-world application, this would likely involve
        # a language model summarization API
        return " ".join([doc['content'] for doc in documents])

if __name__ == "__main__":
    manager = InferenceManager()
    user_query = input("Enter your query: ")
    response = manager.generate_response(user_query)
    print("InsightMate Response:", response)

