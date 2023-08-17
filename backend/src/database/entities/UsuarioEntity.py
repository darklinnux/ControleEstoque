from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.config.base import Base

class UsuarioEntity(Base):
    __tablename__ = 'usuarios'
    usu_id = Column(Integer, primary_key=True, autoincrement=True)
    usu_nome = Column(String)
    usu_cpf = Column(String)
    usu_login = Column(String)
    usu_password = Column(String)
    usu_idperfil = Column(Integer, ForeignKey('departamentos.dep_id'))
    perfil = relationship("CargoEntity", backref="usuario_perfil", lazy="subquery")