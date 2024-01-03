import datetime
import uuid as uuid_pkg

from sqlmodel import TIMESTAMP, Column, Field, ForeignKey, text

from .base import UUIDBaseModel


class LoginRecord(UUIDBaseModel, table=True):
    __tablename__ = "login_record"

    user_id: uuid_pkg.UUID = Field(sa_column=Column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False))
    user_agent: str = Field(nullable=True)
    ip: str = Field(nullable=True)
    access_jti: uuid_pkg.UUID = Field()
    refresh_jti: uuid_pkg.UUID = Field()
    created_at: datetime.datetime = Field(
        sa_column=Column(
            TIMESTAMP(timezone=True),
            nullable=False,
            server_default=text("CURRENT_TIMESTAMP"),
        ),
    )
