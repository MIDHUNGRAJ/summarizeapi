# summarizeapi/core/summarizer.py

from langchain_ollama.llms import OllamaLLM
from langchain_ollama import OllamaEmbeddings


def get_llm():
    return OllamaLLM(model="phi3:mini")


def get_embeddings():
    return OllamaEmbeddings(model="phi3:mini")
