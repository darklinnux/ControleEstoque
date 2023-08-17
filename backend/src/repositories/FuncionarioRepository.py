from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete, update
from sqlalchemy.exc import IntegrityError
from database.connection.ConnectionDB import ConnectionDB
from database.entities.FuncionarioEntity import FuncionarioEntity as Funcionario
from fastapi import HTTPException

class FuncionarioRepository:
    async def insert(fun_nome: str, fun_cpf: str, fun_email: str, fun_matricula: int, fun_idderpatamento: int, fun_idcargo: int):
        async with ConnectionDB() as db:
            try:
                db.session.add(Funcionario(
                    fun_nome = fun_nome,
                    fun_cpf = fun_cpf,
                    fun_email = fun_email,
                    fun_matricula = fun_matricula,
                    fun_idderpatamento = fun_idderpatamento,
                    fun_idcargo = fun_idcargo
                ))
                await db.session.commit()
            except IntegrityError as error:
                raise HTTPException(417, detail={"msg":str("Verificar dados informados"),"error": str(error)})
                        
    async def update(fun_id: int, fun_nome: str, fun_cpf: str, fun_email: str, fun_matricula: int, fun_idderpatamento: int, fun_idcargo: int):
        try:
            async with ConnectionDB() as db:
                await db.session.execute(
                    update(Funcionario).where(Funcionario.fun_id==fun_id).values(
                        fun_nome = fun_nome,
                        fun_cpf = fun_cpf,
                        fun_email = fun_email,
                        fun_matricula = fun_matricula,
                        fun_idderpatamento = fun_idderpatamento,
                        fun_idcargo = fun_idcargo
                    ))
                await db.session.commit()
        except IntegrityError as error:
            raise HTTPException(417, detail={"msg":str("Verificar dados informados"),"error": str(error)})
        
    async def delete(fun_id: int):
        async with ConnectionDB() as db:
            await db.session.execute(
                delete(Funcionario).where(Funcionario.fun_id==fun_id))
            await db.session.commit()

    async def selectAll():
        async with ConnectionDB() as db:
            result = await db.session.execute(select(Funcionario).order_by(Funcionario.fun_id))
            return result.scalars().all()
    
    async def getById(fun_id:int):
        
        async with ConnectionDB() as db:           
            result = await db.session.execute(select(Funcionario).where(Funcionario.fun_id==fun_id))
            funcionario = result.scalar()
            if not isinstance(funcionario, Funcionario):
                raise HTTPException(400, detail={"msg":str("Funcionario não encontrado")})
            return funcionario
