from contextlib import asynccontextmanager
from typing import AsyncIterable

from fastapi import FastAPI

from app.config.settings import settings
from app.infrastructure.db import init_db


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            title=settings.PROJECT_TITLE,
            version=settings.PROJECT_VERSION,
        )
        self._include_routers()

    def _include_routers(self) -> None: ...


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterable:
    await init_db()
    yield


app = App(lifespan=lifespan)
