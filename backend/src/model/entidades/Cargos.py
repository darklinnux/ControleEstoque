from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Cargos(Base):
    __tablename__ = 'cargos'
    car_id = Column(Integer, primary_key=True, autoincrement=True)
    car_nome = Column(String)