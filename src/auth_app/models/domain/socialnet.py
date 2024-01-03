import uuid as uuid_pkg

from pydantic import EmailStr
from sqlmodel import Field

from .base import UUIDBaseModel


class Socialnet(UUIDBaseModel, table=True):
    __tablename__ = "socialnet"

    oauth_id: str = Field(unique=True, index=True, nullable=False)
    email: EmailStr | None = Field(unique=True, nullable=True)

    user_id: uuid_pkg.UUID = Field(foreign_key="user.id")
