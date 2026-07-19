from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app import crud

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/")
def get_dashboard(db: Session = Depends(get_db)):

    stats = crud.get_dashboard_stats(db)

    return {
        "student": "Navya",
        "total_tasks": stats["total_tasks"],
        "completed_tasks": stats["completed_tasks"],
        "pending_tasks": stats["pending_tasks"],
        "today_goal": "Complete Today's Study Plan",
        "message": "Welcome to Student Digital Brain 🚀"
    }