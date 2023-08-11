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

class ProcessadorSchemaOutput(BaseModel):
    pro_modelo: str
    pro_idfabricante: int
    
class ProcessadorSchemaUpdate(BaseModel):
    pro_id: int
    pro_modelo: str
    pro_idfabricante: int
    
class StandardOutput(BaseModel):
    return_request: bool

class ErrorOutput(BaseModel):
    detail: str