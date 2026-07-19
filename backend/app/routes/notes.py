from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud
from app.schemas import NoteCreate

router = APIRouter(
    prefix="/notes",
    tags=["Notes"]
)

@router.post("/add")
def add_note(
    note: NoteCreate,
    db: Session = Depends(get_db)
):

    crud.create_note(db, note)

    return {
        "message":"Note Saved Successfully"
    }


@router.get("/")
def notes(
    db: Session = Depends(get_db)
):

    return crud.get_notes(db)


@router.delete("/{note_id}")
def delete_note(
    note_id:int,
    db:Session=Depends(get_db)
):

    crud.delete_note(db,note_id)

    return {
        "message":"Deleted Successfully"
    }