from typing import List
from fastapi import APIRouter, HTTPException
from schemas.FuncionarioSchema import FuncionarioSchemaList, FuncionarioSchemaInsert, FuncionarioSchemaUpdate
from repositories.FuncionarioRepository import FuncionarioRepository

funcionario_router = APIRouter(prefix='/funcionarios')

@funcionario_router.get('', response_model=List[FuncionarioSchemaList])
async def funcionariosList():
    return await FuncionarioRepository.selectAll()

@funcionario_router.post('')
async def funcionarioInsert(funcionario_input: FuncionarioSchemaInsert):
    await FuncionarioRepository.insert(
            fun_nome = funcionario_input.fun_nome,
            fun_cpf = funcionario_input.fun_cpf,
            fun_email = funcionario_input.fun_email,
            fun_matricula = funcionario_input.fun_matricula,
            fun_idderpatamento = funcionario_input.fun_idderpatamento,
            fun_idcargo = funcionario_input.fun_idcargo
        )
    return {"return":bool(True)}

@funcionario_router.put('')
async def funcionarioUpdate(funcionario_input: FuncionarioSchemaUpdate):
    await FuncionarioRepository.update(
            fun_id = funcionario_input.fun_id,
            fun_nome = funcionario_input.fun_nome,
            fun_cpf = funcionario_input.fun_cpf,
            fun_email = funcionario_input.fun_email,
            fun_matricula = funcionario_input.fun_matricula,
            fun_idderpatamento = funcionario_input.fun_idderpatamento,
            fun_idcargo = funcionario_input.fun_idcargo
        )
    return {"return":bool(True)}

@funcionario_router.get('/{fun_id}')
async def funcionarioList(fun_id:int):
    funcionario = await FuncionarioRepository.getById(fun_id=fun_id)
    return funcionario

@funcionario_router.delete('/{fun_id}')
async def fabricanteDelete(fun_id: int):
    try:
        await FuncionarioRepository.delete(fun_id=fun_id) 
        return {"return":bool(True)}
    except Exception as error:
        raise HTTPException(400, detail=str(error))