
from typing import List
from fastapi import APIRouter, HTTPException
from database.entities.FabricanteEntity import FabricanteEntity
from schemas.FabricanteSchema import FabricanteSchemaList, FabricanteSchemaInsert, FabricanteSchemaUpdate
from schemas.CentroCustoSchema import CentroCustoSchema, CentroCustoSchemaInsert, CentroCustoSchemaUpdate
from repositories.FabricanteRepository import FabricanteRepository
from repositories.CentroCustoRepository import CentroCustoRepository

centroCusto_router = APIRouter(prefix='/centrocusto')

@centroCusto_router.get('', response_model=List[CentroCustoSchema])
async def centroCustoList():
    return await CentroCustoRepository.selectAll()
    

@centroCusto_router.get('/{cen_id}')
async def acessorioList(cen_id:int):
    acessorio = await CentroCustoRepository.getById(cen_id=cen_id)
    return acessorio
    
@centroCusto_router.post('')
async def centroCustoInsert(user_input: CentroCustoSchemaInsert):
    await CentroCustoRepository.insert(cen_nome=user_input.cen_nome)
    return {"return":bool(True)}

@centroCusto_router.put('')
async def centroCustoUpdate(cen_input: CentroCustoSchemaUpdate):
    await CentroCustoRepository.update(cen_id=cen_input.cen_id,cen_nome=cen_input.cen_nome)
    return {"return":bool(True)}


@centroCusto_router.delete('/{cen_id}')
async def fabricanteDelete(cen_id: int):
    try:
        await CentroCustoRepository.delete(cen_id=cen_id) 
        return {"return":bool(True)}
    except Exception as error:
        raise HTTPException(400, detail=str(error))