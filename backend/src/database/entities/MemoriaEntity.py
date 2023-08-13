from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.config.base import Base

class MemoriaEntity(Base):
    __tablename__ = 'memorias'
    mem_id = Column(Integer, primary_key=True, autoincrement=True)
    mem_slot = Column(String)
    mem_capacidade = Column(Integer)
    mem_idfabricante = Column(Integer, ForeignKey('fabricantes.fab_id'))
    fabricante = relationship("FabricanteEntity", backref="Memoria", lazy="subquery")