from sqlalchemy.ext.asyncio import AsyncEngine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from secret_data import USERNAME, PASSWORD, DATABASE

class Base(DeclarativeBase):
    ...


async_engine = f"postgresql+asyncpg://{USERNAME}:{PASSWORD}@5432/{DATABASE}"

Async_session = async_sessionmaker(bind=async_engine)
