
from typing import List
from fastapi import APIRouter, HTTPException
from schemas.AcessorioSchema import AcessorioSchemaList, AcessorioSchemaInsert, AcessorioSchemaUpdate
from repositories.AcessorioRepository import AcessorioRepository

acessorio_router = APIRouter(prefix='/acessorios')

@acessorio_router.get('', response_model=List[AcessorioSchemaList])
async def acessoriosList():

        return await AcessorioRepository.selectAll()

    

@acessorio_router.get('/{ace_id}')
async def acessorioList(ace_id:int):
    try:
        acessorio = await AcessorioRepository.getById(ace_id=ace_id)
        return acessorio
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    
    
@acessorio_router.post('')
async def acessorioInsert(acessorio_input: AcessorioSchemaInsert):
    await AcessorioRepository.insert(
            ace_nome=acessorio_input.ace_nome,
            ace_modelo=acessorio_input.ace_modelo,
            ace_idfabricante=acessorio_input.ace_idfabricante
            )
    return {"return":bool(True)}

@acessorio_router.put('')
async def fabrincanteUpdate(ace_input: AcessorioSchemaUpdate):
    
    await AcessorioRepository.update(ace_id=ace_input.ace_id,ace_nome=ace_input.ace_nome, ace_modelo=ace_input.ace_modelo, ace_idfabricante=ace_input.ace_idfabricante)
    return {"return":bool(True)}

@acessorio_router.delete('/{ace_id}')
async def fabricanteDelete(ace_id: int):
    try:
        await AcessorioRepository.delete(ace_id=ace_id) 
        return {"return":bool(True)}
    except Exception as error:
        raise HTTPException(400, detail=str(error))