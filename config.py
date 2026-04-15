import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecretkey")

    # MySQL connection
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # OpenAI key
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
