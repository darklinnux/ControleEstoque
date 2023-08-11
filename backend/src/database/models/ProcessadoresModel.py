from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection.connection import Base

class ProcessadorModel(Base):
    __tablename__ = 'processadores'
    pro_id = Column(Integer, primary_key=True, autoincrement=True)
    pro_modelo = Column(String)
    pro_idfabricante = Column(Integer, ForeignKey('fabricantes.fab_id'))
    fabricante = relationship("FabricanteModel", backref="Processadores", lazy="subquery",uselist=False)