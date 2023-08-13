from sqlalchemy import Column, Integer, String
from database.config.base import Base

class ProprietarioEntity(Base):
    __tablename__ = 'proprietarios'
    pno_id = Column(Integer, primary_key=True, autoincrement=True)
    pno_nome = Column(String)