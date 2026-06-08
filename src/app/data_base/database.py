from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from secret_data import USERNAME, PASSWORD, DATABASE

URL = f"postgresql+asyncpg://{USERNAME}:{PASSWORD}@5432/{DATABASE}"

async_engine = create_async_engine(
    url=URL,
    pool_size=5,
    max_overflow=30,
    pool_timeout=30,
    echo=False
)

Async_session = async_sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    ...

