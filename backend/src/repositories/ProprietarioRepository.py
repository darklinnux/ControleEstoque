from sqlalchemy.future import select
from sqlalchemy import delete, update
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError, ProgrammingError
from database.entities.ProprietarioEntity import ProprietarioEntity as Proprietario
from database.connection.ConnectionDB import ConnectionDB


class ProprietarioRepository:
    async def insert(pno_nome: str):
        async with ConnectionDB() as db:
            try:
                db.session.add(Proprietario(pno_nome=pno_nome))
                await db.session.commit()
            except IntegrityError as error:
                raise HTTPException(417, detail={"error": str(error)})
            except ProgrammingError as error:
                raise HTTPException(417, detail={"msg":str("Erro de programação"),"error": str(error)})
                        
    async def update(pno_id:int,pno_nome: str):
        async with ConnectionDB() as db:
            try:
                await db.session.execute(
                    update(Proprietario).where(Proprietario.pno_id==pno_id).values(pno_nome=pno_nome))
                await db.session.commit()  
            except IntegrityError as error:
                raise HTTPException(417, detail={"msg":str("Verifique se os dados estão correto"),"error": str(error)})
            except ProgrammingError as error:
                raise HTTPException(417, detail={"msg":str("Erro de programação"),"error": str(error)})            
        
    async def delete(pno_id: int):
        async with ConnectionDB() as db:
            await db.session.execute(
                delete(Proprietario).where(Proprietario.pno_id==pno_id))
            await db.session.commit()

    async def selectAll():
        async with ConnectionDB() as db:
            result = await db.session.execute(select(Proprietario).order_by(Proprietario.pno_id))
            return result.scalars().all()
    
    async def getById(pno_id:int):
        async with ConnectionDB() as db:
            result = await db.session.execute(select(Proprietario).where(Proprietario.pno_id==pno_id))
            proprietario = result.scalar()
            if not isinstance(proprietario, Proprietario):
                raise HTTPException(400, detail={"msg":str("Proprietario não encontrado")})
            return proprietario