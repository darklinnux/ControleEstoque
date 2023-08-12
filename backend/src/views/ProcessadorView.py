
from typing import List
from fastapi import APIRouter, HTTPException
from database.entities.AcessorioEntity import AcessorioEntity
from schemas.AcessorioSchema import AcessorioSchemaList, AcessorioSchemaInsert, AcessorioSchemaUpdate
from schemas.ProcessadorSchema import ProcessadorSchemaList, ProcessadorSchemaInsert, ProcessadorSchemaUpdate
from repositories.AcessorioRepository import AcessorioRepository
from repositories.ProcessadorRepository import ProcessadorRepository

processador_router = APIRouter(prefix='/processadores')

@processador_router.get('', response_model=List[ProcessadorSchemaList])
async def processadorList():
    try:
        return await ProcessadorRepository.selectAll()
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

@processador_router.get('/{pro_id}')
async def processadorList(pro_id:int):
    acessorio = await ProcessadorRepository.getById(pro_id=pro_id)
    return acessorio
    
    
@processador_router.post('')
async def processadorInsert(processador_input: ProcessadorSchemaInsert):
    await ProcessadorRepository.insert(
            pro_modelo=processador_input.pro_modelo,
            pro_idfabricante=processador_input.pro_idfabricante
            )
    return {"return":bool(True)}


@processador_router.put('')
async def processadorUpdate(pro_input: ProcessadorSchemaUpdate):
    
    await ProcessadorRepository.update(pro_id=pro_input.pro_id,pro_modelo=pro_input.pro_modelo, pro_idfabricante=pro_input.pro_idfabricante)
    return {"return":bool(True)}


@processador_router.delete('/{pro_id}')
async def fabricanteDelete(pro_id: int):
    try:
        await ProcessadorRepository.delete(pro_id=pro_id) 
        return {"return":bool(True)}
 
    except Exception as error:
        raise HTTPException(400, detail=str(error))