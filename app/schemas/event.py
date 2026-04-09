from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class EventCreate(BaseModel):
    title: str
    description: Optional[str] = None
    date: Optional[datetime] = None

class EventUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    date: Optional[datetime] = None

class EventResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    date: datetime

    model_config = {"from_attributes": True}