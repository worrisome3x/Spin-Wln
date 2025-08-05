import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.pool import NullPool
from models import Base
from config import Config
import logging

logger = logging.getLogger(__name__)

# Global engine and session maker
engine = None
async_session = None

async def init_db():
    """Initialize database connection and create tables"""
    global engine, async_session
    
    config = Config()
    
    # Convert PostgreSQL URL to async version and remove SSL mode if present
    database_url = config.DATABASE_URL
    if database_url.startswith("postgresql://"):
        database_url = database_url.replace("postgresql://", "postgresql+asyncpg://", 1)
    elif database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql+asyncpg://", 1)
    
    # Remove sslmode parameter as asyncpg handles SSL differently
    if "?sslmode=" in database_url:
        database_url = database_url.split("?sslmode=")[0]
    
    # Create async engine
    engine = create_async_engine(
        database_url,
        poolclass=NullPool,
        echo=False,
        future=True
    )
    
    # Create session maker
    async_session = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False
    )
    
    # Create tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    logger.info("Database initialized successfully")

async def get_db_session():
    """Get database session"""
    if async_session is None:
        await init_db()
    
    async with async_session() as session:
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()

async def get_session():
    """Get a single database session"""
    if async_session is None:
        await init_db()
    return async_session()

async def close_db():
    """Close database connections"""
    global engine
    if engine:
        await engine.dispose()
        logger.info("Database connections closed")
