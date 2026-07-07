from app.config import PROJECT_NAME, VERSION
from fastapi import FastAPI

app = FastAPI(
    title = PROJECT_NAME,
    version = VERSION,
    description = "Backend API for Student Digital Brain Project"
)

#HOME ROUTE
@app.get("/")
def home():
    return {
        "message" : f"Welcome to {PROJECT_NAME} 🚀",
        "version" : VERSION,
        "status" : "Backend Running Successfully"
            }