# SummarizeAPI

A FastAPI-based API service for summarizing text and documents using large language models (LLMs).

Supports running models locally via [Ollama](https://ollama.com) **or** remotely via providers like OpenAI.

Ideal if you want to:

* Summarize arbitrary text
* Summarize uploaded documents (e.g. PDFs)
* Switch easily between local and cloud LLMs

---

## ✨ Features

* Summarize plain text
* Summarize uploaded PDF documents
* Use local Ollama LLMs for private, offline inference
* Or switch to cloud providers (e.g. OpenAI)
* JSON API endpoints
* Built with FastAPI

---

## 🏗️ Project Structure

```
summarizeapi/
├── api/
│   └── v1/
│       ├── routes.py
├── core/
│   ├── llm_factory.py
│   └── summarizer.py
├── models/
│   └── summary_schema.py
├── services/
│   └── pdf_reader.py
├── utils/
│   └── config.py
└── main.py
```

* `main.py` – entry point for FastAPI
* `routes.py` – defines API endpoints
* `llm_factory.py` – handles switching between Ollama / OpenAI / other providers
* `pdf_reader.py` – extracts text from PDF uploads
* `summary_schema.py` – request/response models

---

## 🚀 How it Works

1. **Send plain text**

   * The API summarizes the text using the configured LLM.

2. **Upload a document (PDF)**

   * Text is extracted from the PDF.
   * The LLM summarizes the extracted text (or responds to your custom query).

---

## 🔧 Installation

Clone the repo:

```bash
git clone https://github.com/MIDHUNGRAJ/summarizeapi.git
cd summarizeapi
```

Create a virtual environment and install requirements:

```bash
conda create -n ml-engine python=3.11
conda activate ml-engine

pip install -r requirements.txt
```

---


## 🔗 Running the API

Start the FastAPI server:

```bash
uvicorn summarizeapi.main:app --reload
```

Then visit:

```
http://127.0.0.1:8000/docs
```

to explore the interactive Swagger UI.

---

## 📝 Example API Call

### Summarize Text

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/summarize" \
    -H  "accept: application/json" \
    -H  "Content-Type: multipart/form-data" \
    -F "text=Summarize this text quickly"
```

### Summarize PDF

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/summarize" \
    -H  "accept: application/json" \
    -H  "Content-Type: multipart/form-data" \
    -F "text=Summarize the document content" \
    -F "file=@yourfile.pdf;type=application/pdf"
```

---

## ✅ Todo

* Add support for other document formats (Word, txt, etc.)
* Add support for more LLM providers (Anthropic, Mistral, etc.)
* Implement better error handling
* Add unit tests

---

## License

MIT

