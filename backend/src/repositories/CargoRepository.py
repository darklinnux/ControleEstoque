from sqlalchemy.future import select
from sqlalchemy import delete, update
from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError, ProgrammingError
from database.entities.CargoEntity import CargoEntity as Cargo
from database.connection.ConnectionDB import ConnectionDB


class CargoRepository:
    async def insert(car_nome: str):
        async with ConnectionDB() as db:
            try:
                db.session.add(Cargo(car_nome=car_nome))
                await db.session.commit()
            except IntegrityError as error:
                raise HTTPException(417, detail={"error": str(error)})
            except ProgrammingError as error:
                raise HTTPException(417, detail={"msg":str("Erro de programação"),"error": str(error)})
                        
    async def update(car_id:int,car_nome: str):
        async with ConnectionDB() as db:
            try:
                await db.session.execute(
                    update(Cargo).where(Cargo.car_id==car_id).values(car_nome=car_nome))
                await db.session.commit()  
            except IntegrityError as error:
                raise HTTPException(417, detail={"msg":str("Verifique se os dados estão correto"),"error": str(error)})
            except ProgrammingError as error:
                raise HTTPException(417, detail={"msg":str("Erro de programação"),"error": str(error)})            
        
    async def delete(car_id: int):
        async with ConnectionDB() as db:
            await db.session.execute(
                delete(Cargo).where(Cargo.car_id==car_id))
            await db.session.commit()

    async def selectAll():
        async with ConnectionDB() as db:
            result = await db.session.execute(select(Cargo).order_by(Cargo.car_id))
            return result.scalars().all()
    
    async def getById(car_id:int):
        async with ConnectionDB() as db:
            result = await db.session.execute(select(Cargo).where(Cargo.car_id==car_id))
            cargo = result.scalar()
            if not isinstance(cargo, Cargo):
                raise HTTPException(400, detail={"msg":str("Cargo não encontrado")})
            return cargo