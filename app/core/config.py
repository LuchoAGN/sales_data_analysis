from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Sales Data Analysis API"
    version: str = "0.1.0"

settings = Settings()