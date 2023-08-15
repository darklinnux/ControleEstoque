from sqlalchemy import Column, Integer, String
from database.config.base import Base

class CentroCustoEntity(Base):
    __tablename__ = 'centrocustos'
    cen_id = Column(Integer, primary_key=True, autoincrement=True)
    cen_nome = Column(String)