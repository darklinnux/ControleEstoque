
from typing import List
from fastapi import APIRouter, HTTPException
from database.entities.FabricanteEntity import FabricanteEntity
from schemas.FabricanteSchema import FabricanteSchemaList, FabricanteSchemaInsert, FabricanteSchemaUpdate
from repositories.FabricanteRepository import FabricanteRepository

fabricante_router = APIRouter(prefix='/fabricantes')

@fabricante_router.get('', response_model=List[FabricanteSchemaList])
async def fabricanteList():
    return await FabricanteRepository.selectAll()
    

@fabricante_router.get('/{fab_id}')
async def fabricanteList(fab_id:int):
    try:
        fabricante = await FabricanteRepository.getById(fab_id=fab_id)
        if not isinstance(fabricante, FabricanteEntity):
            raise Exception
        return fabricante
    except Exception as error:
        raise HTTPException(status_code=406, detail={"error":"Não exisite cadastro para o ID informado"})
    
    
@fabricante_router.post('')
async def fabrincanteInsert(user_input: FabricanteSchemaInsert):
    await FabricanteRepository.insert(fab_nome=user_input.fab_nome)
    return {"return":bool(True)}

@fabricante_router.put('')
async def fabrincanteUpdate(fab_input: FabricanteSchemaUpdate):
    await FabricanteRepository.update(fab_id=fab_input.fab_id,fab_nome=fab_input.fab_nome)
    return {"return":bool(True)}


@fabricante_router.delete('/{fab_id}')
async def fabricanteDelete(fab_id: int):
    try:
        await FabricanteRepository.delete(fab_id=fab_id) 
        return {"return":bool(True)}
    except Exception as error:
        raise HTTPException(400, detail=str(error))