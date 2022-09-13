from pydantic import BaseSettings
import secrets


class Settings(BaseSettings):
    # AUTHENTICATION
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    ALGORITHM: str

    # DATABASE SETUP
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    # algorithm: str
    # access_token_expire_minutes: int

    class Config:
        env_file = ".env"


settings = Settings()
