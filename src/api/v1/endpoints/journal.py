from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.core.security import get_current_user
from src.schema.journal import JournalCreate, JournalResponse
from src.crud import journal as journal_crud
from src.models.user import User
from src.core.database import SessionLocal, get_db

router = APIRouter()


@router.post("/journals/")
def create_journal_entry(
        journal: JournalCreate,
        db: Session = Depends(SessionLocal),
        user_id: int = Depends(get_current_user)
):
    db_journal = journal_crud.create_journal_entry(db, journal, user_id)  # Replace with actual user ID
    return db_journal


@router.post("/journals/", response_model=JournalResponse)
def create_journal(journal: JournalCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return create_journal_entry(db=db, journal=journal, user_id=current_user.id)


@router.get("/journals/", response_model=List[JournalResponse])
def get_journals(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return journal_crud.get_journal_entries(db=db, user_id=current_user.id)


@router.delete("/journals/{journal_id}")
def delete_journal(journal_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    journal = journal_crud.get_journal_entry(db=db, journal_id=journal_id, user_id=current_user.id)
    if journal is None:
        raise HTTPException(status_code=404, detail="Journal not found")
    return journal_crud.delete_journal_entry(db=db, journal_id=journal_id, user_id=current_user.id)


@router.get("/journals/", response_model=List[JournalResponse])
def get_journals(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return journal_crud.get_journal_entries(db=db, user_id=current_user.id)