from pydantic import BaseModel
from typing import List
from schemas.FabricanteSchema import FabricanteSchemaList as Fabricante

class DepartamentoSchema(BaseModel):
    dep_id: int
    dep_nome: str
    dep_idcentocusto: int
    class Config:
        from_attributes = True

class DepartamentoSchemaInsert(BaseModel):
    dep_nome: str
    dep_idcentocusto: int
    
class DepartamentoSchemaUpdate(BaseModel):
    dep_id: int
    dep_nome: str
    dep_idcentocusto: int