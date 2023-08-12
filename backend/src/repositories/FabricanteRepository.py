from sqlalchemy.future import select
from sqlalchemy import delete, update
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from database.entities.FabricanteEntity import FabricanteEntity as Fabricante
from database.connection.ConnectionDB import ConnectionDB


class FabricanteRepository:
    async def insert(fab_nome: str):
        async with ConnectionDB() as db:
            try:
                db.session.add(Fabricante(fab_nome=fab_nome))
                await db.session.commit()
            except IntegrityError as error:
                raise HTTPException(417, detail={"msg":str("Não existe o id fabricante cadastrado no banco"),"error": str(error)})
                        
    async def update(fab_id:int,fab_nome: str):
        async with ConnectionDB() as db:
            try:
                await db.session.execute(
                    update(Fabricante).where(Fabricante.fab_id==fab_id).values(fab_nome=fab_nome))
                await db.session.commit()  
            except IntegrityError as error:
                raise HTTPException(417, detail={"msg":str("Verifique se os dados estão correto"),"error": str(error)})            
        
    async def delete(fab_id: int):
        async with ConnectionDB() as db:
            await db.session.execute(
                delete(Fabricante).where(Fabricante.fab_id==fab_id))
            await db.session.commit()

    async def selectAll():
        async with ConnectionDB() as db:
            result = await db.session.execute(select(Fabricante).order_by(Fabricante.fab_id))
            return result.scalars().all()
    
    async def getById(fab_id:int):
        async with ConnectionDB() as db:
            result = await db.session.execute(select(Fabricante).where(Fabricante.fab_id==fab_id))
            fabricante = result.scalar()
            if not isinstance(fabricante, Fabricante):
                raise HTTPException(400, detail={"msg":str("Fabricante não encontrado")})
            return fabricante