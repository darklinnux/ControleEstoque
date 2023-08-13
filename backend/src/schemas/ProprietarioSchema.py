from pydantic import BaseModel
from typing import List


class ProprietarioSchema(BaseModel):
    pno_id: int
    pno_nome: str
    class Config:
        from_attributes = True

class ProprietarioSchemaInsert(BaseModel):
    pno_nome: str
    
class ProprietarioSchemaUpdate(BaseModel):
    pno_id: int
    pno_nome: str
    