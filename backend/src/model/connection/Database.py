from os import getenv

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

class Database():
    def __init__(self):
        self._DATABASE_URL = getenv('DATABASE_URL')
    
    def getConnection(self):
        #abrindo conexão
        engine = create_async_engine(self._DATABASE_URL)
        return sessionmaker(engine, class_=AsyncSession)
        