from sqlalchemy.orm import Session
from app.repositories import registration_repository, event_repository, user_repository

def get_registrations(db: Session):
    return registration_repository.get_all(db)

def create_registration(db: Session, data):
    # cek user
    user = user_repository.get_by_id(db, data.user_id)
    if not user:
        raise Exception("User not found")

    # cek event
    event = event_repository.get_by_id(db, data.event_id)
    if not event:
        raise Exception("Event not found")

    # cek sudah daftar atau belum
    existing = registration_repository.get_by_user_event(
        db, data.user_id, data.event_id
    )
    if existing:
        raise Exception("User already registered")

    # cek quota 🔥
    total = registration_repository.count_by_event(db, data.event_id)
    if total >= event.quota:
        raise Exception("Event quota full")

    return registration_repository.create(db, data)

def delete_registration(db: Session, reg_id: int):
    reg = registration_repository.get_by_id(db, reg_id)
    if not reg:
        raise Exception("Registration not found")
    registration_repository.delete(db, reg)