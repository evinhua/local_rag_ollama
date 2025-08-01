from pydantic import BaseModel, Field
from typing import List, Optional, Union
from datetime import datetime

class DocumentUploadResponse(BaseModel):
    success: bool
    message: str
    document_id: Optional[str] = None
    filename: str
    file_type: str
    chunks_created: Optional[int] = None

class ChatMessage(BaseModel):
    role: str = Field(..., description="Role of the message sender (user/assistant)")
    content: str = Field(..., description="Text content of the message")
    timestamp: datetime = Field(default_factory=datetime.now)
    image_data: Optional[str] = Field(None, description="Base64 encoded image data")

class ChatRequest(BaseModel):
    message: str = Field(..., description="User's text query")
    image_data: Optional[str] = Field(None, description="Base64 encoded image data")
    conversation_history: List[ChatMessage] = Field(default_factory=list)

class ChatResponse(BaseModel):
    response: str
    sources: List[str] = Field(default_factory=list)
    timestamp: datetime = Field(default_factory=datetime.now)

class DocumentChunk(BaseModel):
    id: str
    content: str
    metadata: dict
    embedding: Optional[List[float]] = None

class SearchResult(BaseModel):
    content: str
    metadata: dict
    similarity_score: float

class HealthCheck(BaseModel):
    status: str
    ollama_status: str
    chroma_status: str
    embedding_model: str
    generation_model: str
