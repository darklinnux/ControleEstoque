from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection.connection import Base

class AcessorioModel(Base):
    __tablename__ = 'acessorios'
    ace_id = Column(Integer, primary_key=True, autoincrement=True)
    ace_nome = Column(String)
    ace_modelo = Column(String)
    ace_idfabricante = Column(Integer, ForeignKey('fabricantes.fab_id'))
    fabricante = relationship("FabricanteModel", backref="fabricantes", lazy="subquery")