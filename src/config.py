from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    model:str
    base_url:str

    class Config:
        env_file = "../.env"

SETTINGS = Settings()