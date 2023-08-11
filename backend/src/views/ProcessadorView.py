
from typing import List
from fastapi import APIRouter, HTTPException
from database.models.AcessorioModel import AcessorioModel
from schemas.AcessorioSchema import AcessorioSchemaList, AcessorioSchemaOutput, StandardOutput, ErrorOutput, AcessorioSchemaUpdate
from schemas.ProcessadorSchema import ProcessadorSchemaList, ProcessadorSchemaOutput, ProcessadorSchemaUpdate, StandardOutput, ErrorOutput
from services.AcessorioService import AcessorioService
from services.ProcessadorService import ProcessadorService

processador_router = APIRouter(prefix='/processadores')

@processador_router.get('', response_model=List[ProcessadorSchemaList])
async def processadorList():
    try:
        return await ProcessadorService.selectAll()
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

@processador_router.get('/{ace_id}')
async def acessorioList(ace_id:int):
    acessorio = await AcessorioService.getById(ace_id=ace_id)
    return acessorio
    
    
@processador_router.post('', description='My description', response_model=StandardOutput)
async def acessorioInsert(acessorio_input: AcessorioSchemaOutput):
    await AcessorioService.insert(
            ace_nome=acessorio_input.ace_nome,
            ace_modelo=acessorio_input.ace_modelo,
            ace_idfabricante=acessorio_input.ace_idfabricante
            )
    return StandardOutput(return_request=True)

@processador_router.put('', description='My description', response_model=StandardOutput)
async def fabrincanteUpdate(ace_input: AcessorioSchemaUpdate):
    
    await AcessorioService.update(ace_id=ace_input.ace_id,ace_nome=ace_input.ace_nome, ace_modelo=ace_input.ace_modelo, ace_idfabricante=ace_input.ace_idfabricante)
    return StandardOutput(return_request=True)

@processador_router.delete('/{ace_id}', response_model=StandardOutput, responses={400: {'model': ErrorOutput}})
async def fabricanteDelete(ace_id: int):
    try:
        await AcessorioService.deleteAcessorio(ace_id=ace_id) 
        return StandardOutput(return_request=True) 
    except Exception as error:
        raise HTTPException(400, detail=str(error))