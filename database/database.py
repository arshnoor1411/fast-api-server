from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine
from contextlib import asynccontextmanager


DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/fast-api"

engine = create_async_engine(DATABASE_URL, echo=True)

# Create a configured "sessionmaker" instance
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

@asynccontextmanager
async def get_db():
    async with AsyncSessionLocal() as session:
        try:
            yield session
        finally:
            await session.close()