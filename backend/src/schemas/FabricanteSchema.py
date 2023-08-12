from pydantic import BaseModel
from typing import List


class FabricanteSchemaList(BaseModel):
    fab_id: int
    fab_nome: str
    class Config:
        from_attributes = True

class FabricanteSchemaInsert(BaseModel):
    fab_nome: str
    
class FabricanteSchemaUpdate(BaseModel):
    fab_id: int
    fab_nome: str
    