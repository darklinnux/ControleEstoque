from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

class ConnectionDB:

    def __init__(self) -> None:
        self.__connection_string = 'postgresql+asyncpg://postgres:postgres@engine-bd:5432/bd'
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_async_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    async def __aenter__(self):
        session_make = sessionmaker(self.__engine,class_=AsyncSession)
        self.session = session_make()
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.session.close()