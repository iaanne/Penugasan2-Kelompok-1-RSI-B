from sqlalchemy.orm import Session
from app.repositories import registration_repository, event_repository, user_repository

# Fixed quota per event (adjust as you like)
FIXED_EVENT_QUOTA = 50

def get_registrations(db: Session):
    return registration_repository.get_all(db)

def create_registration(db: Session, data):
    user = user_repository.get_by_id(db, data.user_id)
    if not user:
        raise Exception("User not found")

    event = event_repository.get_by_id(db, data.event_id)
    if not event:
        raise Exception("Event not found")

    existing = registration_repository.get_by_user_event(db, data.user_id, data.event_id)
    if existing:
        raise Exception("User already registered")

    total = registration_repository.count_by_event(db, data.event_id)
    if total >= FIXED_EVENT_QUOTA:
        raise Exception("Event quota full")

    return registration_repository.create(db, data)

def delete_registration(db: Session, reg_id: int):
    reg = registration_repository.get_by_id(db, reg_id)
    if not reg:
        raise Exception("Registration not found")
    registration_repository.delete(db, reg)

def get_live_blog(db: Session):
    rows = registration_repository.get_live_blog(db)

    result = []
    for reg, user, event in rows:
        result.append({
            "event_name": getattr(event, "name", "Unnamed Event"),
            "user_name": user.first_name,
            "registered_at": reg.created_at
        })

    return result