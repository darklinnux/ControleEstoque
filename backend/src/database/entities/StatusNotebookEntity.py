from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.connection.connection import Base

class StatusNotebookEntity(Base):
    __tablename__ = 'statusnotebook'
    sta_id = Column(Integer, primary_key=True, autoincrement=True)
    sta_nome = Column(String)