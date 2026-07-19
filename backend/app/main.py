from app.config import PROJECT_NAME, VERSION
from fastapi import FastAPI
from app.routes.users import router as user_router
from app.database import Base, engine
from app import models
from app.routes.dashboard import router as dashboard_router
from app.routes.tasks import router as task_router
from app.routes.recommend import router as recommend_router
from app.routes.notes import router as notes_router

app = FastAPI(
    title = PROJECT_NAME,
    version = VERSION,
    description = "Backend API for Student Digital Brain Project"
)

app.include_router(dashboard_router)
app.include_router(task_router)

Base.metadata.create_all(bind=engine)
app.include_router(user_router)

app.include_router(recommend_router)

app.include_router(notes_router)
#HOME ROUTE
@app.get("/")
def home():
    return {
        "message" : f"Welcome to {PROJECT_NAME} 🚀",
        "version" : VERSION,
        "status" : "Backend Running Successfully"
            }