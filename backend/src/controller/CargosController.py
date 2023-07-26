from model.connection.Database import Database
from model.entidades.Cargos import Cargos

class CargosController():
    async def create_user(name: str):
        database = Database()
        async with database.getConnection() as session:
            session.add(Cargos(name=name))
            await session.commit()