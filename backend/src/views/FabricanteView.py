
from typing import List
from fastapi import APIRouter, HTTPException
from starlette import responses
from schemas.FabricanteSchema import FabricanteSchemaList, FabricanteSchemaOutput, StandardOutput, ErrorOutput, FabricanteSchemaUpdate
from services.FabricanteService import FabricanteService

fabricante_router = APIRouter(prefix='/fabricantes')

@fabricante_router.get('', response_model=List[FabricanteSchemaList])
async def fabricanteList():
    try:
        return await FabricanteService.selectAll()
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@fabricante_router.get('/{fab_id}', response_model=FabricanteSchemaList)
async def fabricanteList(fab_id:int):
    try:
        return await FabricanteService.getById(fab_id=fab_id)
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
@fabricante_router.post('', description='My description', response_model=StandardOutput)
async def fabrincanteInsert(user_input: FabricanteSchemaOutput):
    try:
        await FabricanteService.insert(fab_nome=user_input.fab_nome)
        return StandardOutput(return_request=True)
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@fabricante_router.put('', description='My description', response_model=StandardOutput)
async def fabrincanteInsert(fab_input: FabricanteSchemaUpdate):
    try:
        await FabricanteService.update(fab_id=fab_input.fab_id,fab_nome=fab_input.fab_nome)
        return StandardOutput(return_request=True)
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@fabricante_router.delete('/{fab_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def fabricanteDelete(fab_id: int):
    try:
        await FabricanteService.deleteFrabricante(fab_id=fab_id) 
        return StandardOutput(return_request=True) 
    except Exception as error:
        raise HTTPException(400, detail=str(error))