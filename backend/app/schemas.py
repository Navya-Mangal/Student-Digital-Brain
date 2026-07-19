from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email:EmailStr
    password:str

class TaskCreate(BaseModel):
    title: str
    subject: str
    priority: str
    deadline: str

class RecommendationInput(BaseModel):

    gender: str
    age: int
    college_year: str
    branch: str
    cgpa: float
    attendance_percentage: float
    study_hours_per_day: float
    weekly_study_hours: float
    quiz_score: float
    assignment_score: float
    exam_score: float
    coding_score: float
    problem_solving_score: float
    logical_reasoning_score: float
    communication_score: float
    notes_completion_percentage: float
    revision_sessions_per_week: int
    tasks_completed: int
    tasks_pending: int
    daily_screen_time_hours: float
    social_media_hours: float
    sleep_hours: float
    stress_level: float
    focus_level: float
    motivation_level: float

class NoteCreate(BaseModel):

    title: str

    content: str

    subject: str