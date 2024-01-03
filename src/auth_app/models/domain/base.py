import uuid as uuid_pkg

from sqlmodel import Column, Field, SQLModel, text
from sqlmodel.sql.sqltypes import GUID


class UUIDBaseModel(SQLModel):
    id: uuid_pkg.UUID = Field(
        sa_column=Column(
            GUID,
            server_default=text("gen_random_uuid()"),
            primary_key=True,
            index=True,
            nullable=False,
        ),
    )
