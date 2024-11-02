from typing import List, Union, ClassVar

from pydantic_settings import BaseSettings
from pydantic import Field, validator


def get_api_version() -> str:
    with open("version") as version:
        return version.readline()


class APISettings(BaseSettings):    
    TITLE: str = "API Cowhub"
    HOST: str = "127.0.0.1"
    PORT: int = 8000
    LOG_LEVEL: str = "info"
    VERSION: str = get_api_version()
    TIME_ZONE: str = "America/Recife"
    CORS_ORIGINS: Union[str, List[str]] = Field(..., env="API_CORS_ORIGINS")

    @validator("CORS_ORIGINS", pre=True)
    def _assemble_cors_origins(cls, cors_origins):
        if isinstance(cors_origins, str):
            return [item.strip() for item in cors_origins.split(",")]
        return cors_origins

    class Config:
        env_prefix = "API_"


class DatabaseSettings(BaseSettings):
    URL: str = "postgresql://user:password@host:port/dbname"

    class Config:
        env_prefix = "DATABASE_"


class SMTPSettings(BaseSettings):
    PORT: int = 587
    HOST: str = "localhost"
    USER: str = "user@user.com"
    PASSWORD: str = "123456"
    EMAIL_COMPANY: ClassVar[str] =  "joseluan@gmail.com"

    class Config:
        env_prefix = "SMTP_"


api_settings = APISettings()
database_settings = DatabaseSettings()
smtp_settings = SMTPSettings()
