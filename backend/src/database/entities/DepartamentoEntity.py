from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.config.base import Base

class DepartamentoEntity(Base):
    __tablename__ = 'departamentos'
    dep_id = Column(Integer, primary_key=True, autoincrement=True)
    dep_nome = Column(String)
    dep_idcentocusto = Column(Integer, ForeignKey('centrocustos.cen_id'))
    centrocusto = relationship("CentroCustoEntity", backref="centrocusto", lazy="subquery")