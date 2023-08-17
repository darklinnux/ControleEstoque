from sqlalchemy import Column, Integer, String
from database.config.base import Base

class PerfilEntity(Base):
    __tablename__ = 'perfis'
    per_id = Column(Integer, primary_key=True, autoincrement=True)
    per_nome = Column(String)
