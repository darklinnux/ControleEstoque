
from typing import List
from fastapi import APIRouter, HTTPException
from schemas.CargoSchema import CargoSchema, CargoSchemaInsert, CargoSchemaUpdate
from repositories.CargoRepository import CargoRepository

cargo_router = APIRouter(prefix='/cargos')

@cargo_router.get('', response_model=List[CargoSchema])
async def cargoList():
    return await CargoRepository.selectAll()
    

@cargo_router.get('/{car_id}')
async def cargoList(car_id:int):
    
    return await CargoRepository.getById(car_id=car_id)
       
@cargo_router.post('')
async def cargoInsert(proprietario_input: CargoSchemaInsert):
    await CargoRepository.insert(car_nome=proprietario_input.car_nome)
    return {"return":bool(True)}

@cargo_router.put('')
async def cargoUpdate(fab_input: CargoSchemaUpdate):
    await CargoRepository.update(car_id=fab_input.car_id,car_nome=fab_input.car_nome)
    return {"return":bool(True)}

@cargo_router.delete('/{car_id}')
async def cargoDelete(car_id: int):
    try:
        await CargoRepository.delete(car_id=car_id) 
        return {"return":bool(True)}
    except Exception as error:
        raise HTTPException(400, detail=str(error))