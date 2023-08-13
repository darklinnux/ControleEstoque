
from typing import List
from fastapi import APIRouter, HTTPException
from schemas.ProprietarioSchema import ProprietarioSchema, ProprietarioSchemaInsert, ProprietarioSchemaUpdate
from repositories.ProprietarioRepository import ProprietarioRepository

proprietario_router = APIRouter(prefix='/proprietarios')

@proprietario_router.get('', response_model=List[ProprietarioSchema])
async def proprietarioList():
    return await ProprietarioRepository.selectAll()
    

@proprietario_router.get('/{pno_id}')
async def proprietarioList(pno_id:int):
    
    return await ProprietarioRepository.getById(pno_id=pno_id)
       
@proprietario_router.post('')
async def fabrincanteInsert(proprietario_input: ProprietarioSchemaInsert):
    await ProprietarioRepository.insert(pno_nome=proprietario_input.pno_nome)
    return {"return":bool(True)}

@proprietario_router.put('')
async def fabrincanteUpdate(fab_input: ProprietarioSchemaUpdate):
    await ProprietarioRepository.update(pno_id=fab_input.pno_id,pno_nome=fab_input.pno_nome)
    return {"return":bool(True)}

@proprietario_router.delete('/{pno_id}')
async def fabricanteDelete(pno_id: int):
    try:
        await ProprietarioRepository.delete(pno_id=pno_id) 
        return {"return":bool(True)}
    except Exception as error:
        raise HTTPException(400, detail=str(error))