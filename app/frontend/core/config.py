from pydantic import BaseSettings
from dotenv import load_dotenv
from pathlib import Path


load_dotenv(Path(__file__).parent / "front.env")


class Settings(BaseSettings):
    api_url: "http://127.0.0.1:8000/"


settings = Settings()
