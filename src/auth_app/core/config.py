from datetime import timedelta
from logging import config as logging_config
from pathlib import Path

from pydantic import BaseSettings, Field, PostgresDsn

from .logger import get_logging_settings


class JaegerSettings(BaseSettings):
    host: str = Field()
    port: int = Field()

    class Config:
        env_file = ".env"
        env_prefix = "auth_jaeger_"


class RedisSettings(BaseSettings):
    host: str = Field()
    port: int = Field()

    class Config:
        env_file = ".env"
        env_prefix = "auth_redis_"


class PostgresSettings(BaseSettings):
    user: str = Field()
    password: str = Field()
    host: str = Field()
    port: int = Field()
    db: str = Field()

    class Config:
        env_file = ".env"
        env_prefix = "auth_postgres_"


class GoogleOAuthSettings(BaseSettings):
    client_id: str = Field()
    client_secret: str = Field()

    class Config:
        env_file = ".env"
        env_prefix = "auth_google_"


class YandexOAuthSettings(BaseSettings):
    client_id: str = Field()
    client_secret: str = Field()

    class Config:
        env_file = ".env"
        env_prefix = "auth_yandex_"


class OAuthSettings(BaseSettings):
    google = GoogleOAuthSettings()
    yandex = YandexOAuthSettings()


class Settings(BaseSettings):
    project_name: str = Field()
    jaeger = JaegerSettings()
    redis = RedisSettings()
    db = PostgresSettings()
    oauth = OAuthSettings()
    database_dsn: PostgresDsn = f"postgresql+asyncpg://{db.user}:{db.password}@{db.host}:{db.port}/{db.db}"

    rsa_public_path: Path = Field()
    rsa_private_path: Path = Field()

    logging_level: str = Field("INFO")
    console_logging_level: str = Field("DEBUG")
    debug_mode: bool = Field(False)

    access_token_lifetime: timedelta = Field("P0DT12H00M0S")
    refresh_token_lifetime: timedelta = Field("P15DT12H00M0S")

    request_limit_per_minute: int = Field(60)

    debug: bool = Field(False)

    class Config:
        env_file = ".env"
        env_prefix = "auth_"


BASE_DIR = Path(__file__).parent.parent
settings = Settings()  # type: ignore

logging_config.dictConfig(
    get_logging_settings(
        settings.logging_level,
        settings.console_logging_level,
    ),
)
