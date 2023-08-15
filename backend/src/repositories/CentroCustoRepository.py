from sqlalchemy.future import select
from sqlalchemy import delete, update
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError
from database.entities.CentroCustoEntity import CentroCustoEntity as CentroCusto
from database.connection.ConnectionDB import ConnectionDB


class CentroCustoRepository:
    async def insert(cen_nome: str):
        async with ConnectionDB() as db:
            try:
                db.session.add(CentroCusto(cen_nome=cen_nome))
                await db.session.commit()
            except IntegrityError as error:
                raise HTTPException(417, detail={"msg":str("Não existe o id centro de custo cadastrado no banco"),"error": str(error)})
                        
    async def update(cen_id:int,cen_nome: str):
        async with ConnectionDB() as db:
            try:
                await db.session.execute(
                    update(CentroCusto).where(CentroCusto.cen_id==cen_id).values(cen_nome=cen_nome))
                await db.session.commit()  
            except IntegrityError as error:
                raise HTTPException(417, detail={"msg":str("Verifique se os dados estão correto"),"error": str(error)})            
        
    async def delete(cen_id: int):
        async with ConnectionDB() as db:
            await db.session.execute(
                delete(CentroCusto).where(CentroCusto.cen_id==cen_id))
            await db.session.commit()

    async def selectAll():
        async with ConnectionDB() as db:
            result = await db.session.execute(select(CentroCusto).order_by(CentroCusto.cen_id))
            return result.scalars().all()
    
    async def getById(cen_id:int):
        async with ConnectionDB() as db:
            result = await db.session.execute(select(CentroCusto).where(CentroCusto.cen_id==cen_id))
            centroDeCusto = result.scalar()
            if not isinstance(centroDeCusto, CentroCusto):
                raise HTTPException(400, detail={"msg":str("CentroCusto não encontrado")})
            return centroDeCusto