from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete, update

from database.models.FabricanteModel import FabricanteModel as Fabricante
from database.connection.connection import async_session


class FabricanteService:
    async def insert(fab_nome: str):
        async with async_session() as session:
            session.add(Fabricante(fab_nome=fab_nome))
            await session.commit()
            
    async def update(fab_id:int,fab_nome: str):
        async with async_session() as session:
            await session.execute(
                update(Fabricante).where(Fabricante.fab_id==fab_id).values(fab_nome=fab_nome))
            await session.commit()   
        
    async def deleteFrabricante(fab_id: int):
        async with async_session() as session:
            await session.execute(
                delete(Fabricante).where(Fabricante.fab_id==fab_id))
            await session.commit()

    async def selectAll():
        async with async_session() as session:
            result = await session.execute(select(Fabricante).order_by(Fabricante.fab_id))
            return result.scalars().all()
    
    async def getById(fab_id:int):
        async with async_session() as session:
            result = await session.execute(select(Fabricante).where(Fabricante.fab_id==fab_id))
            return result.scalar()