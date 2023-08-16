from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.config.base import Base

class FuncionarioEntity(Base):
    __tablename__ = 'funcionarios'
    fun_id = Column(Integer, primary_key=True, autoincrement=True)
    fun_nome = Column(String)
    fun_cpf = Column(String)
    fun_email = Column(String)
    fun_matricula = Column(Integer)
    fun_idderpatamento = Column(Integer, ForeignKey('departamentos.dep_id'))
    departamento = relationship("DepartamentoEntity", backref="funcionarios_dep", lazy="subquery")
    fun_idcargo = Column(Integer, ForeignKey('cargos.car_id'))
    cargo = relationship("CargoEntity", backref="funcionarios_cargo", lazy="subquery")