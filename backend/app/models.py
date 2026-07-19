from sqlalchemy import Column, Integer, String
from app.database import Base
class User(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

class Task(Base):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    subject = Column(String, nullable=False)

    priority = Column(String, nullable=False)

    status = Column(String, default="Pending")

    deadline = Column(String)

    user_id = Column(Integer)

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String)

    content = Column(String)

    subject = Column(String)

    user_id = Column(Integer)