from sqlalchemy import bindparam
from sqlalchemy.orm import Session
from src.models.journal import Journal
from src.schema.journal import JournalCreate


def create_journal_entry(db: Session, journal: JournalCreate, user_id: int):
    db_journal = Journal(**journal.dict(), user_id=user_id)
    db.add(db_journal)
    db.commit()
    db.refresh(db_journal)
    return db_journal


def delete_journal_entry(db: Session, journal_id: int, user_id: int):
    db_journal = db.query(Journal).filter(
        Journal.id == bindparam('journal_id', value=journal_id),
        Journal.user_id == bindparam('user_id', value=user_id)
    ).first()
    if db_journal:
        db.delete(db_journal)
        db.commit()
        return db_journal
    return None


# Might have to use bindparam
def get_journal_entries(db: Session, user_id: int):
    return db.query(Journal).filter(Journal.user_id == user_id).all()


def get_journal_entry(db: Session, journal_id: int, user_id: int):
    return db.query(Journal).filter(
        Journal.id == bindparam('journal_id', value=journal_id),
        Journal.user_id == bindparam('user_id', value=user_id)
    ).first()



