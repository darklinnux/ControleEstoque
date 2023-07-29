from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()

class NotebookModel(Base):
    __tablename__ = 'notebooks'
    not_id = Column(Integer, primary_key=True, autoincrement=True)
    not_nome = Column(String)
