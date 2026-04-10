from pickle import FALSE
from typing import List
from pydantic_settings import BaseSettings
from pydantic import field_validator

class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = FALSE
    DATABASE_URL: str  = ""
    OPENAI_API_KEY:str
    @field_validator("ALLOWED_ORIGINS")
    def validate_allowed_origins(cls, v) -> List[str]:
        return v.split(",") if v else []

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
settings = Settings()
    
