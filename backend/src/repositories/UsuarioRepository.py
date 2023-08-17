from sqlalchemy.ext.asyncio.session import async_session
from sqlalchemy.future import select
from sqlalchemy import delete, update
from sqlalchemy.exc import IntegrityError
from database.connection.ConnectionDB import ConnectionDB
from database.entities.UsuarioEntity import UsuarioEntity as Usuario
from fastapi import HTTPException

class UsuarioRepository:
    async def insert(usu_id: str, usu_nome: str, usu_cpf: str, usu_login: int, usu_password: int, usu_idperfil: int):
        async with ConnectionDB() as db:
            try:
                db.session.add(Usuario(
                    usu_nome = usu_nome,
                    usu_cpf = usu_cpf,
                    usu_login = usu_login,
                    usu_password = usu_password,
                    usu_idperfil = usu_idperfil,
                ))
                await db.session.commit()
            except IntegrityError as error:
                raise HTTPException(417, detail={"msg":str("Verificar dados informados"),"error": str(error)})
                        
    async def update(usu_id: int, usu_nome: str, usu_cpf: str, usu_login: str, usu_password: int, usu_idperfil: int):
        try:
            async with ConnectionDB() as db:
                await db.session.execute(
                    update(Usuario).where(Usuario.usu_id==usu_id).values(
                        usu_nome = usu_nome,
                        usu_cpf = usu_cpf,
                        usu_login = usu_login,
                        usu_password = usu_password,
                        usu_idperfil = usu_idperfil,
                    ))
                await db.session.commit()
        except IntegrityError as error:
            raise HTTPException(417, detail={"msg":str("Verificar dados informados"),"error": str(error)})
        
    async def delete(usu_id: int):
        async with ConnectionDB() as db:
            await db.session.execute(
                delete(Usuario).where(Usuario.usu_id==usu_id))
            await db.session.commit()

    async def selectAll():
        async with ConnectionDB() as db:
            result = await db.session.execute(select(Usuario).order_by(Usuario.usu_id))
            return result.scalars().all()
    
    async def getById(usu_id:int):
        
        async with ConnectionDB() as db:           
            result = await db.session.execute(select(Usuario).where(Usuario.usu_id==usu_id))
            usuario = result.scalar()
            if not isinstance(usuario, Usuario):
                raise HTTPException(400, detail={"msg":str("Usuario não encontrado")})
            return usuario
