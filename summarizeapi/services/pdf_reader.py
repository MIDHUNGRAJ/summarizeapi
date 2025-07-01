import tempfile
import os
from langchain_community.document_loaders import PyPDFLoader


def extract_text_from_pdf(uploaded_file):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file)
        temp_path = tmp.name

    loader = PyPDFLoader(temp_path)
    pages = loader.load()

    os.remove(temp_path)

    return pages
