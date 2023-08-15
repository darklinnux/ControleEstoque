from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete, update
from sqlalchemy.exc import IntegrityError
from database.entities.DepartamentoEntity import DepartamentoEntity as Departamento
from database.connection.ConnectionDB import ConnectionDB
from fastapi import HTTPException

class DepartamentoRepository:
    async def insert(dep_nome: str, dep_idcentocusto: int):
        async with ConnectionDB() as db:
            try:
                db.session.add(Departamento(
                dep_nome=dep_nome,
                dep_idcentocusto=dep_idcentocusto))
                await db.session.commit()
            except IntegrityError as error:
                raise HTTPException(417, detail={"msg":str("Não existe o id departamento cadastrado no banco"),"error": str(error)})
                        
    async def update(dep_id:int,dep_nome: str, dep_idcentocusto: int):
        try:
            async with ConnectionDB() as db:
                await db.session.execute(
                    update(Departamento).where(Departamento.dep_id==dep_id).values(
                        dep_nome=dep_nome, dep_idcentocusto = dep_idcentocusto))
                await db.session.commit()
        except IntegrityError as error:
            raise HTTPException(417, detail={"msg":str("Não existe o id departamento cadastrado no banco"),"error": str(error)})
        
    async def delete(dep_id: int):
        async with ConnectionDB() as db:
            await db.session.execute(
                delete(Departamento).where(Departamento.dep_id==dep_id))
            await db.session.commit()

    async def selectAll():
        async with ConnectionDB() as db:
            result = await db.session.execute(select(Departamento).order_by(Departamento.dep_id))
            return result.scalars().all()
    
    async def getById(dep_id:int):
        
        async with ConnectionDB() as db:           
            result = await db.session.execute(select(Departamento).where(Departamento.dep_id==dep_id))
            departamento = result.scalar()
            if not isinstance(departamento, Departamento):
                raise HTTPException(400, detail={"msg":str("Departamento não encontrado")})
            return departamento
