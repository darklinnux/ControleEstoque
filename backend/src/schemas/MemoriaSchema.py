from pydantic import BaseModel
from typing import List
from schemas.FabricanteSchema import FabricanteSchemaList as Fabricante

class MemoriaSchema(BaseModel):
    mem_id: int
    mem_slot: str
    mem_capacidade: int
    mem_idfabricante: int
    fabricante: Fabricante
    class Config:
        from_attributes = True

class MemoriaSchemaInsert(BaseModel):
    mem_slot: str
    mem_capacidade: int
    mem_idfabricante: int
    
class MemoriaSchemaUpdate(BaseModel):
    mem_id: int
    mem_slot: str
    mem_capacidade: int
    mem_idfabricante: int