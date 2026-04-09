from pickle import FALSE
from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = FALSE
    DATABASE_URL: str 
    OPENAI_API_KEY:str
    @field_validator("ALLOWED_ORIGINS")
    
