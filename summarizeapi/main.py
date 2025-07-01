# summarizeapi/summarizeapi/main.py

from fastapi import FastAPI
from summarizeapi.api.v1.routes import router as v1_router

app = FastAPI(
    title="SummarizeAPI",
    version="1.0.0",
    description="API for summarizing text and documents"
)

app.include_router(v1_router, prefix="/api/v1")
