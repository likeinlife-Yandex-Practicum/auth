from typing import TYPE_CHECKING

from pydantic import EmailStr
from sqlmodel import Field, Relationship

from .base import UUIDBaseModel
from .user_role import UserRole

if TYPE_CHECKING:
    from .role import Role
    from .socialnet import Socialnet


class User(UUIDBaseModel, table=True):
    __tablename__ = "user"

    email: EmailStr = Field(unique=True, index=True, nullable=False)
    hashed_password: str = Field(max_length=256, min_length=8, nullable=False)

    roles: list["Role"] = Relationship(
        link_model=UserRole,
        back_populates="users",
        sa_relationship_kwargs={"cascade": "all, delete"},
    )
    socialnet: list["Socialnet"] = Relationship(
        sa_relationship_kwargs={"cascade": "all, delete"},
    )
