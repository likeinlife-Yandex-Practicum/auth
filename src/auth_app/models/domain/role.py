from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship

from .base import UUIDBaseModel
from .user_role import UserRole

if TYPE_CHECKING:
    from .user import User


class Role(UUIDBaseModel, table=True):
    __tablename__ = "role"

    name: str = Field(max_length=256, unique=True, nullable=False)
    description: str | None = Field(max_length=256)

    users: list["User"] = Relationship(link_model=UserRole, back_populates="roles")
