from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
)

@router.post("/add")
def add_task(task: schemas.TaskCreate,
             db: Session = Depends(get_db)):

    new_task = crud.create_task(db, task)

    return {
        "message": "Task Added Successfully",
        "task": {
            "id": new_task.id,
            "title": new_task.title,
            "subject": new_task.subject,
            "priority": new_task.priority,
            "status": new_task.status,
            "deadline": new_task.deadline
        }
    }

@router.get("/")
def get_tasks(db: Session = Depends(get_db)):

    tasks = crud.get_all_tasks(db)

    return {
        "total_tasks": len(tasks),
        "tasks": tasks
    }

@router.put("/complete/{task_id}")
def mark_complete(task_id: int,
                  db: Session = Depends(get_db)):

    task = crud.complete_task(db, task_id)

    if task is None:
        return {
            "message": "Task Not Found"
        }

    return {
        "message": "Task Completed Successfully",
        "task": task
    }

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):

    task = crud.delete_task(db, task_id)

    if task is None:
        return {
            "message": "Task Not Found"
        }

    return {
        "message": "Task Deleted Successfully"
    }