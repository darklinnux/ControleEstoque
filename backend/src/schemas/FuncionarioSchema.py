from pydantic import BaseModel
from typing import List
from schemas.DepartamentoSchema import DepartamentoSchema as Departamento
from schemas.CargoSchema import CargoSchema as Cargo

class FuncionarioSchemaList(BaseModel):
    fun_id: int
    fun_nome: str
    fun_cpf: str
    fun_email: str
    fun_matricula: int
    fun_idderpatamento: int
    departamento: Departamento
    fun_idcargo: int
    cargo: Cargo
    class Config:
        from_attributes = True

class FuncionarioSchemaInsert(BaseModel):
    fun_nome: str
    fun_cpf: str
    fun_email: str
    fun_matricula: int
    fun_idderpatamento: int
    fun_idcargo: int
    
class FuncionarioSchemaUpdate(BaseModel):
    fun_id: int
    fun_nome: str
    fun_cpf: str
    fun_email: str
    fun_matricula: int
    fun_idderpatamento: int
    fun_idcargo: int