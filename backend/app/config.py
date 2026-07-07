from dotenv import load_dotenv
import os
#load .env file
load_dotenv()

#Read environment variables
PROJECT_NAME = os.getenv("PROJECT_NAME")
VERSION = os.getenv("VERSION")
DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")