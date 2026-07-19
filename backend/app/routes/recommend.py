from fastapi import APIRouter
from app.schemas import RecommendationInput

router = APIRouter(
    prefix="/recommend",
    tags=["AI Recommendation"]
)

@router.post("/")
def recommend(student: RecommendationInput):

    recommendation = ""
    reason = ""

    if student.attendance_percentage < 75:
        recommendation = "Improve Attendance"
        reason = "Your attendance is below 75%."

    elif student.coding_score < 60:
        recommendation = "Practice Coding"
        reason = "Your coding score is low."

    elif student.assignment_score < 60:
        recommendation = "Complete Assignments"
        reason = "Assignment performance needs improvement."

    elif student.quiz_score < 60:
        recommendation = "Take More Quizzes"
        reason = "Quiz score is below average."

    elif student.study_hours_per_day < 3:
        recommendation = "Increase Study Hours"
        reason = "Daily study hours are less than recommended."

    elif student.stress_level > 8:
        recommendation = "Take a Break"
        reason = "Your stress level is very high."

    elif student.focus_level < 5:
        recommendation = "Improve Focus"
        reason = "Focus level is low."

    elif student.notes_completion_percentage < 60:
        recommendation = "Complete Your Notes"
        reason = "Notes completion is low."

    else:
        recommendation = "Keep Up the Good Work"
        reason = "Your academic performance looks balanced."

    return {
        "recommendation": recommendation,
        "reason": reason,
        "confidence": "90%"
    }