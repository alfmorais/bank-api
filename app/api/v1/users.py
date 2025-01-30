from fastapi import APIRouter, Depends, status
from sqlmodel.ext.asyncio.session import AsyncSession

from app.domain.entities.user import (
    UserMessageResponse,
    UserRequest,
    UserResponse,
)
from app.domain.services.auth_service import get_password_hash
from app.infrastructure.db import get_session
from app.infrastructure.repositories.user_repository import UserRepository

users_routers = APIRouter(
    prefix="/v1/users",
    tags=["Users"],
)


@users_routers.post(
    "",
    response_model=UserMessageResponse,
    status_code=status.HTTP_201_CREATED,
    description="Endpoint para criar um usuario",
)
async def create(
    user: UserRequest,
    session: AsyncSession = Depends(get_session),
):
    repository = UserRepository(db=session)
    hashed_password = get_password_hash(password=user.password)
    return await repository.create_user(user=user, hashed_password=hashed_password)


@users_routers.get(
    "/{username}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    description="Endpoint para listar um usuario pelo username",
)
async def get_user_by_username(
    username: str,
    session: AsyncSession = Depends(get_session),
):
    repository = UserRepository(db=session)
    return await repository.get_user_by_username(username=username)


@users_routers.get(
    "/{id}",
    response_model=UserResponse,
    status_code=status.HTTP_200_OK,
    description="Endpoint para listar um usuario pelo id",
)
async def get_user_by_id(
    id: str,
    session: AsyncSession = Depends(get_session),
):
    repository = UserRepository(db=session)
    return await repository.get_user_by_id(id=id)
