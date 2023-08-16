from pydantic import BaseModel
from typing import List
from schemas.CentroCustoSchema import CentroCustoSchema as CentroCusto

class DepartamentoSchema(BaseModel):
    dep_id: int
    dep_nome: str
    dep_idcentocusto: int
    centrocusto: CentroCusto
    class Config:
        from_attributes = True

class DepartamentoSchemaInsert(BaseModel):
    dep_nome: str
    dep_idcentocusto: int
    
class DepartamentoSchemaUpdate(BaseModel):
    dep_id: int
    dep_nome: str
    dep_idcentocusto: int