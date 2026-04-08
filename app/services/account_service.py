from sqlalchemy.orm import Session
from app.repositories import account_repository, user_repository, role_repository

def get_accounts(db: Session):
    return account_repository.get_all(db)

def get_account(db: Session, account_id: int):
    account = account_repository.get_by_id(db, account_id)
    if not account:
        raise Exception("Account not found")
    return account

def create_account(db: Session, data):
    # VALIDASI RELASI 🔥
    user = user_repository.get_by_id(db, data.user_id)
    if not user:
        raise Exception("User not found")

    role = role_repository.get_by_id(db, data.role_id)
    if not role:
        raise Exception("Role not found")

    return account_repository.create(db, data)

def update_account(db: Session, account_id: int, data):
    account = account_repository.get_by_id(db, account_id)
    if not account:
        raise Exception("Account not found")

    return account_repository.update(db, account, data)

def delete_account(db: Session, account_id: int):
    account = account_repository.get_by_id(db, account_id)
    if not account:
        raise Exception("Account not found")
    account_repository.delete(db, account)