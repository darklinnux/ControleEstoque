from pydantic import BaseModel
from typing import List
from schemas.FabricanteSchema import FabricanteSchemaList as Fabricante

class ProcessadorSchemaList(BaseModel):
    pro_id: int
    pro_modelo: str
    pro_idfabricante: int
    fabricante: Fabricante
    class Config:
        from_attributes = True

class ProcessadorSchemaInsert(BaseModel):
    pro_modelo: str
    pro_idfabricante: int
    
class ProcessadorSchemaUpdate(BaseModel):
    pro_id: int
    pro_modelo: str
    pro_idfabricante: int