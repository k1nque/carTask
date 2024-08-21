import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USERNAME: str
    POSTGRES_PASSWORD: str
    SECRET_KEY: str
    ALGORITHM: str

    # model_config = SettingsConfigDict(
    #     env_file=os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
    # )


settings = Settings()


def get_db_url():
    return (
        f"postgresql+asyncpg://{settings.POSTGRES_USERNAME}:{settings.POSTGRES_PASSWORD}@"
        f"{settings.POSTGRES_HOST}:{settings.POSTGRES_PORT}"
    )

    
def get_auth_data():
    return {"secret_key": settings.SECRET_KEY, "algorithm": settings.ALGORITHM}