from pydantic import BaseModel
from typing import List


class PerfilSchema(BaseModel):
    car_id: int
    car_nome: str
    class Config:
        from_attributes = True

class PerfilSchemaInsert(BaseModel):
    car_nome: str
    
class PerfilSchemaUpdate(BaseModel):
    car_id: int
    car_nome: str
    