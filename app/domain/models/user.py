import uuid

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: uuid.UUID = Field(default=uuid.uuid4, primary_key=True)
    username: str = Field(sa_column=Field(unique=True))
    full_name: str
    email: EmailStr
    hashed_password: str
