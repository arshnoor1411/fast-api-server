from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager


DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/fast-api"

engine = create_async_engine(DATABASE_URL, echo=True)

# Create a configured "sessionmaker" instance
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
        await session.commit()