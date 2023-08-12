from sqlalchemy import Column, Integer, String
from database.config.base import Base

class FabricanteEntity(Base):
    __tablename__ = 'fabricantes'
    fab_id = Column(Integer, primary_key=True, autoincrement=True)
    fab_nome = Column(String)
