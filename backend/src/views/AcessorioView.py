
from typing import List
from fastapi import APIRouter, HTTPException
from database.models.AcessorioModel import AcessorioModel
from schemas.AcessorioSchema import AcessorioSchemaList, AcessorioSchemaOutput, StandardOutput, ErrorOutput, AcessorioSchemaUpdate
from services.FabricanteService import FabricanteService
from services.AcessorioService import AcessorioService

acessorio_router = APIRouter(prefix='/acessorios')

@acessorio_router.get('', response_model=List[AcessorioSchemaList])
async def acessoriosList():

        return await AcessorioService.selectAll()

    

@acessorio_router.get('/{ace_id}')
async def acessorioList(ace_id:int):
    try:
        
        acessorio = await AcessorioService.getById(ace_id=ace_id)
        return acessorio
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
    
@acessorio_router.post('', description='My description', response_model=StandardOutput)
async def acessorioInsert(acessorio_input: AcessorioSchemaOutput):
    await AcessorioService.insert(
            ace_nome=acessorio_input.ace_nome,
            ace_modelo=acessorio_input.ace_modelo,
            ace_idfabricante=acessorio_input.ace_idfabricante
            )
    return StandardOutput(return_request=True)

@acessorio_router.put('', description='My description', response_model=StandardOutput)
async def fabrincanteUpdate(ace_input: AcessorioSchemaUpdate):
    
    await AcessorioService.update(ace_id=ace_input.ace_id,ace_nome=ace_input.ace_nome, ace_modelo=ace_input.ace_modelo, ace_idfabricante=ace_input.ace_idfabricante)
    return StandardOutput(return_request=True)

@acessorio_router.delete('/{ace_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def fabricanteDelete(ace_id: int):
    try:
        await AcessorioService.deleteAcessorio(ace_id=ace_id) 
        return StandardOutput(return_request=True) 
    except Exception as error:
        raise HTTPException(400, detail=str(error))