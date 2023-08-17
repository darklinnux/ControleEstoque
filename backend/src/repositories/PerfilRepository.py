from fastapi import HTTPException
from sqlalchemy.future import select
from database.entities.PerfilEntity import PerfilEntity as Perfil
from database.connection.ConnectionDB import ConnectionDB

class PerfilRepository:
    async def selectAll():
        async with ConnectionDB() as db:
            try:
                result = await db.session.execute(select(Perfil).order_by(Perfil.per_id))
                return result
            except Exception as error:
                raise HTTPException(400, detail={"msg":str(error)})
    
    async def getById(per_id:int):
        
        async with ConnectionDB() as db:           
            result = await db.session.execute(select(Perfil).where(Perfil.per_id==per_id))
            perfil = result.scalar()
            if not isinstance(perfil, Perfil):
                raise HTTPException(400, detail={"msg":str("Perfil não encontrado")})
            return perfil
