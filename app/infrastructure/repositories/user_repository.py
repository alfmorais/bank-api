from sqlmodel import select
from sqlmodel.ext.asyncio.session import AsyncSession

from app.domain.entities.user import UserRequest
from app.domain.models.user import User


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user: UserRequest, hashed_password: str) -> dict:
        user = User(
            username=user.username,
            full_name=user.full_name,
            email=user.email,
            hashed_password=hashed_password,
        )
        self.db.add(user)
        await self.db.commit()
        await self.db.refresh(user)
        response = {"message": "User successfully created", "id": user.id}
        return response

    async def get_user_by_username(self, username: str) -> User:
        statement = select(User).where(User.username == username)
        user = await self.db.exec(statement=statement)
        return user.one_or_none()

    async def get_user_by_id(self, id: int) -> User:
        statement = select(User).where(User.id == id)
        user = await self.db.exec(statement=statement)
        return user.one_or_none()
