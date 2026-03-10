from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str

    admin_username: str
    admin_password: str

    cors_origins: str = ""
    reservation_slot_capacity: int = 3

    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()
