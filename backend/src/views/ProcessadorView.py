
from typing import List
from fastapi import APIRouter, HTTPException
from database.entities.AcessorioEntity import AcessorioEntity
from schemas.AcessorioSchema import AcessorioSchemaList, AcessorioSchemaInsert, AcessorioSchemaUpdate
from schemas.ProcessadorSchema import ProcessadorSchemaList, ProcessadorSchemaOutput, ProcessadorSchemaUpdate
from repositories.AcessorioRepository import AcessorioRepository
from repositories.ProcessadorRepository import ProcessadorService

processador_router = APIRouter(prefix='/processadores')

@processador_router.get('', response_model=List[ProcessadorSchemaList])
async def processadorList():
    try:
        return await ProcessadorService.selectAll()
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

@processador_router.get('/{ace_id}')
async def acessorioList(ace_id:int):
    acessorio = await AcessorioRepository.getById(ace_id=ace_id)
    return acessorio
    
    
@processador_router.post('')
async def acessorioInsert(acessorio_input: AcessorioSchemaInsert):
    await AcessorioRepository.insert(
            ace_nome=acessorio_input.ace_nome,
            ace_modelo=acessorio_input.ace_modelo,
            ace_idfabricante=acessorio_input.ace_idfabricante
            )
    return StandardOutput(return_request=True)

@processador_router.put('')
async def fabrincanteUpdate(ace_input: AcessorioSchemaUpdate):
    
    await AcessorioRepository.update(ace_id=ace_input.ace_id,ace_nome=ace_input.ace_nome, ace_modelo=ace_input.ace_modelo, ace_idfabricante=ace_input.ace_idfabricante)
    return StandardOutput(return_request=True)

@processador_router.delete('/{ace_id}')
async def fabricanteDelete(ace_id: int):
    try:
        await AcessorioRepository.delete(ace_id=ace_id) 
        return StandardOutput(return_request=True) 
    except Exception as error:
        raise HTTPException(400, detail=str(error))