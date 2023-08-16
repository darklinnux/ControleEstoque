from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.config.base import Base

class FuncionarioEntity(Base):
    __tablename__ = 'acessorios'
    fun_id = Column(Integer, primary_key=True, autoincrement=True)
    fun_nome = Column(String)
    fun_cpf = Column(String)
    fun_email = Column(Integer, ForeignKey('fabricantes.fab_id'))
    fun_matricula = relationship("FabricanteEntity", backref="fabricantes", lazy="subquery")
    fun_iddepartamento = None
    departamento = relationship("FabricanteEntity", backref="fabricantes", lazy="subquery")
    fun_idCargo = None
    cargo = relationship("FabricanteEntity", backref="fabricantes", lazy="subquery")