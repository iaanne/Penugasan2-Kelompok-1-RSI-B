from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.event import EventCreate, EventUpdate, EventResponse
from app.services import event_service

router = APIRouter(prefix="/events", tags=["Events"])

@router.get("/", response_model=list[EventResponse])
def get_events(db: Session = Depends(get_db)):
    return event_service.get_events(db)

@router.get("/{event_id}", response_model=EventResponse)
def get_event(event_id: int, db: Session = Depends(get_db)):
    try:
        return event_service.get_event(db, event_id)
    except:
        raise HTTPException(status_code=404, detail="Event not found")

@router.post("/", response_model=EventResponse)
def create_event(data: EventCreate, db: Session = Depends(get_db)):
    return event_service.create_event(db, data)

@router.put("/{event_id}", response_model=EventResponse)
def update_event(event_id: int, data: EventUpdate, db: Session = Depends(get_db)):
    try:
        return event_service.update_event(db, event_id, data)
    except:
        raise HTTPException(status_code=404, detail="Event not found")

@router.delete("/{event_id}")
def delete_event(event_id: int, db: Session = Depends(get_db)):
    try:
        event_service.delete_event(db, event_id)
        return {"message": "Event deleted"}
    except:
        raise HTTPException(status_code=404, detail="Event not found")