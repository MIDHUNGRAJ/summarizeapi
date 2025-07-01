# summarizeapi/models/summary_schema.py

from pydantic import BaseModel


class SummaryRequest(BaseModel):
    text: str


class SummaryResponse(BaseModel):
    summary: str
