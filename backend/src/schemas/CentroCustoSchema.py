from pydantic import BaseModel
from typing import List


class CentroCustoSchema(BaseModel):
    cen_id: int
    cen_nome: str
    class Config:
        from_attributes = True

class CentroCustoSchemaInsert(BaseModel):
    cen_nome: str
    
class CentroCustoSchemaUpdate(BaseModel):
    cen_id: int
    cen_nome: str
    