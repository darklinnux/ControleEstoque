
from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.exceptions import ResponseValidationError
from starlette import responses
from database.models.FabricanteModel import FabricanteModel
from database.models.AcessorioModel import AcessorioModel
from schemas.FabricanteSchema import FabricanteSchemaList, FabricanteSchemaOutput, StandardOutput, ErrorOutput, FabricanteSchemaUpdate
from schemas.AcessorioSchema import AcessorioSchemaList, AcessorioSchemaOutput, StandardOutput, ErrorOutput, AcessorioSchemaUpdate
from services.FabricanteService import FabricanteService
from services.AcessorioService import AcessorioService

acessorio_router = APIRouter(prefix='/acessorios')

@acessorio_router.get('', response_model=List[AcessorioSchemaList])
async def acessoriosList():
    try:
        return await AcessorioService.selectAll()
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

@acessorio_router.get('/{ace_id}')
async def acessorioList(ace_id:int):
    try:
        acessorio = await AcessorioService.getById(ace_id=ace_id)
        if not isinstance(acessorio, AcessorioModel):
            raise Exception
        return acessorio
    except Exception as error:
        raise HTTPException(status_code=406, detail={"error":"Não exisite cadastro para o ID informado"})
    
    
@acessorio_router.post('', description='My description', response_model=StandardOutput)
async def acessorioInsert(acessorio_input: AcessorioSchemaOutput):
    try:
        await AcessorioService.insert(
            ace_nome=acessorio_input.ace_nome,
            ace_modelo=acessorio_input.ace_modelo,
            ace_idfabricante=acessorio_input.ace_idfabricante
            )
        return StandardOutput(return_request=True)
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@acessorio_router.put('', description='My description', response_model=StandardOutput)
async def fabrincanteUpdate(fab_input: FabricanteSchemaUpdate):
    try:
        await FabricanteService.update(fab_id=fab_input.fab_id,fab_nome=fab_input.fab_nome)
        return StandardOutput(return_request=True)
    
    except Exception as error:
        raise HTTPException(400, detail=str(error))

@acessorio_router.delete('/{fab_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def fabricanteDelete(fab_id: int):
    try:
        await FabricanteService.deleteFrabricante(fab_id=fab_id) 
        return StandardOutput(return_request=True) 
    except Exception as error:
        raise HTTPException(400, detail=str(error))