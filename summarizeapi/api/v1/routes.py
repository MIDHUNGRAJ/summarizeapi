from fastapi import APIRouter, UploadFile, File, Form
from summarizeapi.core.summarizer import get_llm, get_embeddings
from summarizeapi.models.summary_schema import SummaryResponse
from summarizeapi.services.pdf_reader import extract_text_from_pdf
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain.chains import RetrievalQA

router = APIRouter()

llm = get_llm()
embeddings = get_embeddings()


@router.post("/summarize", response_model=SummaryResponse)
async def summarize(text: str = Form(None), file: UploadFile = File(None)):
    if file is not None:
        # → Summarize Document Flow
        file_data = await file.read()
        pages = extract_text_from_pdf(file_data)
        splitter = RecursiveCharacterTextSplitter(chunk_size=1000,
                                                  chunk_overlap=200)
        docs = splitter.split_documents(pages)

        vectorstore = InMemoryVectorStore.from_documents(
            documents=docs, embedding=embeddings
        )
        retriever = vectorstore.as_retriever()

        qa_chain = RetrievalQA.from_chain_type(
            llm=llm, chain_type="stuff", retriever=retriever
        )

        # Either use user's question, or default to summarization
        query = text or "Summarize this document."
        result = qa_chain.invoke({"query": query})

        return SummaryResponse(summary=result["result"])

    elif text is not None:
        # → Summarize Text Flow
        result = llm.invoke(f"Summarize this: {text}")
        return SummaryResponse(summary=result)

    else:
        return SummaryResponse(summary="No text or document provided.")
