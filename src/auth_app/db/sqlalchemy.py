from sqlalchemy.orm import sessionmaker
from sqlmodel.ext.asyncio.session import AsyncEngine, AsyncSession

engine: AsyncEngine | None = None


async def get_async_session() -> AsyncSession:
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    async with async_session() as session:
        yield session
