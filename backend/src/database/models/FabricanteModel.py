from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class FabricanteModel(Base):
    __tablename__ = 'fabricantes'
    fab_id = Column(Integer, primary_key=True, autoincrement=True)
    fab_nome = Column(String)
