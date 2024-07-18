import os
from pathlib import Path

from dotenv import load_dotenv

env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path, override=True)


class Settings:
    PROJECT_NAME: str = "Debates App"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER: str = os.getenv("DB_USER")
    POSTGRES_PASSWORD = os.getenv("DB_USER_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("DB_HOST", "localhost")
    POSTGRES_PORT: str = os.getenv("DB_PORT", 5432)
    POSTGRES_DB: str = os.getenv("DB_NAME")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


settings = Settings()
