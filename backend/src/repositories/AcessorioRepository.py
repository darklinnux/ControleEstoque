from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete, update
from sqlalchemy.exc import IntegrityError
from database.entities.AcessorioEntity import AcessorioEntity as Acessorio
from database.connection.ConnectionDB import ConnectionDB
from fastapi import HTTPException

class AcessorioRepository:
    async def insert(ace_nome: str, ace_modelo: str, ace_idfabricante: int):
        async with ConnectionDB() as db:
            try:
                db.session.add(Acessorio(
                ace_nome=ace_nome,
                ace_modelo=ace_modelo,
                ace_idfabricante=ace_idfabricante))
                await db.session.commit()
            except IntegrityError as error:
                raise HTTPException(417, detail={"msg":str("Não existe o id fabricante cadastrado no banco"),"error": str(error)})
                        
    async def update(ace_id:int,ace_nome: str, ace_modelo: str, ace_idfabricante: int):
        try:
            async with ConnectionDB() as db:
                await db.session.execute(
                    update(Acessorio).where(Acessorio.ace_id==ace_id).values(
                        ace_nome=ace_nome, ace_modelo = ace_modelo, ace_idfabricante = ace_idfabricante))
                await db.session.commit()
        except IntegrityError as error:
            raise HTTPException(417, detail={"msg":str("Não existe o id fabricante cadastrado no banco"),"error": str(error)})
        
    async def delete(ace_id: int):
        async with ConnectionDB() as db:
            await db.session.execute(
                delete(Acessorio).where(Acessorio.ace_id==ace_id))
            await db.session.commit()

    async def selectAll():
        async with ConnectionDB() as db:
            result = await db.session.execute(select(Acessorio).order_by(Acessorio.ace_id))
            return result.scalars().all()
    
    async def getById(ace_id:int):
        
        async with ConnectionDB() as db:           
            result = await db.session.execute(select(Acessorio).where(Acessorio.ace_id==ace_id))
            acessorio = result.scalar()
            if not isinstance(acessorio, Acessorio):
                raise HTTPException(400, detail={"msg":str("Acessório não encontrado")})
            return acessorio
