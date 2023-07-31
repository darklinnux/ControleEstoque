from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete, update

from database.models.AcessorioModel import AcessorioModel as Acessorio
from database.connection.connection import async_session


class AcessorioService:
    async def insert(ace_nome: str, ace_modelo: str, ace_idfabricante: int):
        async with async_session() as session:
            session.add(Acessorio(
                ace_nome=ace_nome,
                ace_modelo=ace_modelo,
                ace_idfabricante=ace_idfabricante))
            await session.commit()
            
    async def update(ace_id:int,ace_nome: str, ace_modelo: str, ace_idfabricante: str):
        async with async_session() as session:
            await session.execute(
                update(Acessorio).where(Acessorio.ace_id==ace_id).values(
                    ace_nome=ace_nome, ace_modelo = ace_modelo, ace_idfabricante = ace_idfabricante))
            await session.commit()   
        
    async def deleteAcessorio(ace_id: int):
        async with async_session() as session:
            await session.execute(
                delete(Acessorio).where(Acessorio.ace_id==ace_id))
            await session.commit()

    async def selectAll():
        async with async_session() as session:
            result = await session.execute(select(Acessorio).order_by(Acessorio.ace_id))
            return result.scalars().all()
    
    async def getById(ace_id:int):
        async with async_session() as session:
            result = await session.execute(select(Acessorio).where(Acessorio.ace_id==ace_id))
            return result.scalar()