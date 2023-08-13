
from typing import List
from fastapi import APIRouter, HTTPException
from schemas.MemoriaSchema import MemoriaSchema, MemoriaSchemaInsert,MemoriaSchemaUpdate
from repositories.MemoriaRepository import MemoriaRepository

memoria_router = APIRouter(prefix='/memorias')

@memoria_router.get('', response_model=List[MemoriaSchema])
async def acessoriosList():

        return await MemoriaRepository.selectAll()

    

@memoria_router.get('/{mem_id}')
async def acessorioList(mem_id:int):
    memoria = await MemoriaRepository.getById(mem_id=mem_id)
    return memoria
    
@memoria_router.post('')
async def acessorioInsert(memoria_input: MemoriaSchemaInsert):
    await MemoriaRepository.insert(
            mem_slot=memoria_input.mem_slot,
            mem_capacidade=memoria_input.mem_capacidade,
            mem_idfabricante=memoria_input.mem_idfabricante
            )
    return {"return":bool(True)}

@memoria_router.put('')
async def fabrincanteUpdate(mem_input: MemoriaSchemaUpdate):
    
    await MemoriaRepository.update(
        mem_id=mem_input.mem_id,
        mem_slot=mem_input.mem_slot,
        mem_capacidade=mem_input.mem_capacidade, 
        mem_idfabricante=mem_input.mem_idfabricante
        )
    return {"return":bool(True)}

@memoria_router.delete('/{mem_id}')
async def fabricanteDelete(mem_id: int):
    try:
        await MemoriaRepository.delete(mem_id=mem_id) 
        return {"return":bool(True)}
    except Exception as error:
        raise HTTPException(400, detail=str(error))