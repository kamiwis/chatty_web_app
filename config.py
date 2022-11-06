import os
from dotenv import load_dotenv
from pathlib import Path

# Set path to env file.
env_path = Path(".") / ".env"
# Get environment variables from .env
load_dotenv(dotenv_path=env_path)


class Config:
    """Set configuration variables from .env"""

    # Save env variables
    TESTING = os.getenv("TESTING")
    DEBUG = os.getenv("DEBUG")
    SECRET_KEY = os.getenv("SECRET_KEY")
    SERVER = os.getenv("SERVER")
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
