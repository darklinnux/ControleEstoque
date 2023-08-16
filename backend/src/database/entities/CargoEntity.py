from sqlalchemy import Column, Integer, String
from database.config.base import Base

class CargoEntity(Base):
    __tablename__ = 'cargos'
    car_id = Column(Integer, primary_key=True, autoincrement=True)
    car_nome = Column(String)
