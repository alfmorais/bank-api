import uuid

from pydantic import BaseModel, EmailStr


class UserRequest(BaseModel):
    username: str
    full_name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: uuid.UUID
    message: str
