from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.schemas import UserCreate
from app import crud, schemas
from app.database import get_db

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):

    new_user = crud.create_user(db, user)

    return {
        "message": "User Registered Successfully",
        "id": new_user.id,
        "name": new_user.name,
        "email": new_user.email
    }
# @router.get("/")
# def get_users():
#     return {
#         "message": "List of users will be shown here."
#     }

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):

    db_user = crud.login_user(db, user)

    if db_user is None:
        return {
            "message": "Invalid Email or Password"
        }
    
    return {
        "message": "Login Successful",
        "user":{
            "id": db_user.id,
            "name": db_user.name,
            "email": db_user.email
        }
    }