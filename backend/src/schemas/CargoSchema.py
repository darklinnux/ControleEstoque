from pydantic import BaseModel
from typing import List


class CargoSchema(BaseModel):
    car_id: int
    car_nome: str
    class Config:
        from_attributes = True

class CargoSchemaInsert(BaseModel):
    car_nome: str
    
class CargoSchemaUpdate(BaseModel):
    car_id: int
    car_nome: str
    