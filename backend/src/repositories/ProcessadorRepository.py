from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete, update
from sqlalchemy.exc import IntegrityError
from database.entities.ProcessadoresEntity import ProcessadorEntity as Processador
from database.connection.ConnectionDB import ConnectionDB
from fastapi import HTTPException

class ProcessadorService:
    async def insert(pro_modelo: str, pro_idfabricante: int):
        async with ConnectionDB() as db:
            try:
                db.session.add(Processador(
                pro_modelo=pro_modelo,
                pro_idfabricante=pro_idfabricante))
                await db.session.commit()
            except IntegrityError as error:
                raise HTTPException(417, detail={"msg":str("Não existe o id fabricante cadastrado no banco"),"error": str(error)})
                
            
    async def update(pro_id:int,pro_modelo: str, pro_idfabricante: int):
        try:
            async with ConnectionDB() as db:
                await db.session.execute(
                    update(Processador).where(Processador.pro_id==pro_id).values(
                        pro_modelo = pro_modelo, pro_idfabricante = pro_idfabricante))
                await db.session.commit()
        except IntegrityError as error:
            raise HTTPException(417, detail={"msg":str("Não existe o id fabricante cadastrado no banco"),"error": str(error)})
        
    async def deleteProcessador(pro_id: int):
        async with ConnectionDB() as db:
            await db.session.execute(
                delete(Processador).where(Processador.pro_id==pro_id))
            await db.session.commit()

    async def selectAll():
        async with ConnectionDB() as db:
            result = await db.session.execute(select(Processador).order_by(Processador.pro_id))
            return result.scalars().all()
    
    async def getById(ace_id:int):
        
        async with ConnectionDB() as db:           
            result = await db.session.execute(select(Processador).where(Processador.ace_id==ace_id))
            processador = result.scalar()
            if not isinstance(processador, Processador):
                raise HTTPException(400, detail={"msg":str("Processador não encontrado")})
            return processador
