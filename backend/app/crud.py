from sqlalchemy.orm import Session
from app import models, schemas
from sqlalchemy import func

def create_user(db: Session, user: schemas.UserCreate):

    db_user = models.User(
        name=user.name,
        email=user.email,
        password=user.password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def login_user(db: Session, user: schemas.UserLogin):

    db_user = (
        db.query(models.User)
        .filter(models.User.email == user.email)
        .first()
    )

    if not db_user:
        return None
    
    if db_user.password != user.password:
        return None
    
    return db_user

def create_task(db: Session, task: schemas.TaskCreate):

    db_task = models.Task(
        title=task.title,
        subject=task.subject,
        priority=task.priority,
        deadline=task.deadline
    )

    db.add(db_task)
    db.commit()
    db.refresh(db_task)

    return db_task

def get_all_tasks(db: Session):
    return db.query(models.Task).all()

def complete_task(db: Session, task_id: int):

    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task is None:
        return None

    task.status = "Completed"

    db.commit()
    db.refresh(task)

    return task

def delete_task(db: Session, task_id: int):

    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task is None:
        return None

    db.delete(task)
    db.commit()

    return task

def get_dashboard_stats(db: Session):

    total = db.query(models.Task).count()

    completed = (
        db.query(models.Task)
        .filter(models.Task.status == "Completed")
        .count()
    )

    pending = (
        db.query(models.Task)
        .filter(models.Task.status == "Pending")
        .count()
    )

    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending
    }

def create_note(db, note):

    new_note = models.Note(

        title=note.title,

        content=note.content,

        subject=note.subject,

        user_id=1
    )

    db.add(new_note)

    db.commit()

    db.refresh(new_note)

    return new_note


def get_notes(db):

    return db.query(models.Note).all()


def delete_note(db, note_id):

    note = db.query(models.Note).filter(
        models.Note.id == note_id
    ).first()

    if note:

        db.delete(note)

        db.commit()