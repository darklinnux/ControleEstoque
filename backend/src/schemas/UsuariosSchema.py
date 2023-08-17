from pydantic import BaseModel
from typing import List
from schemas.DepartamentoSchema import DepartamentoSchema as Departamento
from schemas.CargoSchema import CargoSchema as Cargo

class UsuarioSchemaList(BaseModel):
    usu_id: int
    usu_nome: str
    usu_cpf: str
    fun_email: str
    usu_login: int
    usu_password: int
    usu_idperfil: Departamento
    fun_idcargo: int
    cargo: Cargo
    class Config:
        from_attributes = True

class UsuarioSchemaInsert(BaseModel):
    fun_nome: str
    fun_cpf: str
    fun_email: str
    fun_matricula: int
    fun_idderpatamento: int
    fun_idcargo: int
    
class UsuarioSchemaUpdate(BaseModel):
    fun_id: int
    fun_nome: str
    fun_cpf: str
    fun_email: str
    fun_matricula: int
    fun_idderpatamento: int
    fun_idcargo: int