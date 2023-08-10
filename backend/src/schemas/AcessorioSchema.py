from pydantic import BaseModel
from typing import List
from schemas.FabricanteSchema import FabricanteSchemaList as Fabricante

class AcessorioSchemaList(BaseModel):
    ace_id: int
    ace_nome: str
    ace_modelo: str
    ace_idfabricante: int
    fabricante: Fabricante
    class Config:
        from_attributes = True

class AcessorioSchemaOutput(BaseModel):
    ace_nome: str
    ace_modelo: str
    ace_idfabricante: int
    
class AcessorioSchemaUpdate(BaseModel):
    ace_id: int
    ace_nome: str
    ace_modelo: str
    ace_idfabricante: int
    
class StandardOutput(BaseModel):
    return_request: bool

class ErrorOutput(BaseModel):
    detail: str