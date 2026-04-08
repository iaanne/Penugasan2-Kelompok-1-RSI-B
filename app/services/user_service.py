from sqlalchemy.orm import Session
from app.repositories import user_repository

def get_users(db: Session):
    return user_repository.get_all(db)

def get_user(db: Session, user_id: int):
    user = user_repository.get_by_id(db, user_id)
    if not user:
        raise Exception("User not found")
    return user

def create_user(db: Session, data):
    return user_repository.create(db, data)

def update_user(db: Session, user_id: int, data):
    user = user_repository.get_by_id(db, user_id)
    if not user:
        raise Exception("User not found")
    return user_repository.update(db, user, data)

def delete_user(db: Session, user_id: int):
    user = user_repository.get_by_id(db, user_id)
    if not user:
        raise Exception("User not found")
    user_repository.delete(db, user)