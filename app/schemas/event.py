from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EventCreate(BaseModel):
    name: str
    description: str
    quota: int
    started_at: datetime
    ended_at: datetime

class EventUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    quota: Optional[int] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None

class EventResponse(BaseModel):
    id: int
    name: str
    description: str
    quota: int
    started_at: datetime
    ended_at: datetime
    created_at: datetime

    model_config = {"from_attributes": True}
