from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any

class LogEntry(BaseModel):
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    level: str
    service_name: str
    message: str
    metaData: Optional[Dict[str, Any]] = None

class AnalysisRequest(BaseModel):
    question: str
    time_window_minutes: int= 60