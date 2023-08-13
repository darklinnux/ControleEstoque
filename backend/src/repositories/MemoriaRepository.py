from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete, update
from sqlalchemy.exc import IntegrityError, ProgrammingError
from database.entities.MemoriaEntity import MemoriaEntity as Memoria
from database.connection.ConnectionDB import ConnectionDB
from fastapi import HTTPException

class MemoriaRepository:
    async def insert(mem_slot: str, mem_capacidade: str, mem_idfabricante: int):
        async with ConnectionDB() as db:
            try:
                db.session.add(Memoria(
                mem_slot=mem_slot,
                mem_capacidade=mem_capacidade,
                mem_idfabricante=mem_idfabricante))
                await db.session.commit()
            except IntegrityError as error:
                raise HTTPException(417, detail={"msg":str("Não existe o id fabricante cadastrado no banco"),"error": str(error)})
            except ProgrammingError as error:
                raise HTTPException(417, detail={"msg":str("Erro de programação"),"error": str(error)})
                        
    async def update(mem_id:int,mem_slot: str, mem_capacidade: str, mem_idfabricante: int):
        try:
            async with ConnectionDB() as db:
                await db.session.execute(
                    update(Memoria).where(Memoria.mem_id==mem_id).values(
                        mem_slot=mem_slot, mem_capacidade = mem_capacidade, mem_idfabricante = mem_idfabricante))
                await db.session.commit()
        except IntegrityError as error:
            raise HTTPException(417, detail={"msg":str("Não existe o id fabricante cadastrado no banco"),"error": str(error)})
        
    async def delete(mem_id: int):
        async with ConnectionDB() as db:
            await db.session.execute(
                delete(Memoria).where(Memoria.mem_id==mem_id))
            await db.session.commit()

    async def selectAll():
        async with ConnectionDB() as db:
            result = await db.session.execute(select(Memoria).order_by(Memoria.mem_id))
            return result.scalars().all()
    
    async def getById(mem_id:int):
        
        async with ConnectionDB() as db:           
            result = await db.session.execute(select(Memoria).where(Memoria.mem_id==mem_id))
            memoria = result.scalar()
            if not isinstance(memoria, Memoria):
                raise HTTPException(400, detail={"msg":str("Memoria não encontrado")})
            return memoria
