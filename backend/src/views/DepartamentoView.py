
from typing import List
from fastapi import APIRouter, HTTPException
from schemas.DepartamentoSchema import DepartamentoSchema, DepartamentoSchemaInsert, DepartamentoSchemaUpdate
from repositories.DepartamentoRepository import DepartamentoRepository

departamento_router = APIRouter(prefix='/departamentos')

@departamento_router.get('', response_model=List[DepartamentoSchema])
async def departamentoList():
    try:
        return await DepartamentoRepository.selectAll()
    except Exception as error:
        raise HTTPException(400, detail=str(error))
    

@departamento_router.get('/{dep_id}')
async def departamentoList(dep_id:int):
    acessorio = await DepartamentoRepository.getById(dep_id=dep_id)
    return acessorio
    
    
@departamento_router.post('')
async def departamentoInsert(processador_input: DepartamentoSchemaInsert):
    await DepartamentoRepository.insert(
            dep_nome=processador_input.dep_nome,
            dep_idcentocusto=processador_input.dep_idcentocusto
            )
    return {"return":bool(True)}


@departamento_router.put('')
async def departamentoUpdate(dep_id: DepartamentoSchemaUpdate):
    
    await DepartamentoRepository.update(dep_id=dep_id.dep_id,dep_nome=dep_id.dep_nome, dep_idcentocusto=dep_id.dep_idcentocusto)
    return {"return":bool(True)}


@departamento_router.delete('/{dep_id}')
async def departamentoDelete(dep_id: int):
    try:
        await DepartamentoRepository.delete(dep_id=dep_id) 
        return {"return":bool(True)}
 
    except Exception as error:
        raise HTTPException(400, detail=str(error))