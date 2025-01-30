
from pydantic import BaseModel, ConfigDict, EmailStr


class UserRequest(BaseModel):
    username: str
    full_name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    model_config = ConfigDict(extra="ignore")

    id: int
    username: str
    full_name: str
    email: EmailStr


class UserMessageResponse(BaseModel):
    id: int
    message: str
