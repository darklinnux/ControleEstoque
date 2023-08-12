from fastapi import HTTPException
from sqlalchemy.future import select
from database.entities.ProcessadoresEntity import ProcessadorEntity as Processador
from database.entities.StatusNotebookEntity import StatusNotebookEntity as StatusNotebook
from database.connection.ConnectionDB import ConnectionDB

class StatusNotebookRepository:
    async def selectAll():
        async with ConnectionDB() as db:
            try:
                result = await db.session.execute(select(StatusNotebook).order_by(StatusNotebook.sta_id))
                return result
            except Exception as error:
                raise HTTPException(400, detail={"msg":str(error)})
    
    async def getById(sta_id:int):
        
        async with ConnectionDB() as db:           
            result = await db.session.execute(select(StatusNotebook).where(StatusNotebook.sta_id==sta_id))
            statusNotebook = result.scalar()
            if not isinstance(statusNotebook, StatusNotebook):
                raise HTTPException(400, detail={"msg":str("Status não encontrado")})
            return statusNotebook
