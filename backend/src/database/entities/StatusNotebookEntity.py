from sqlalchemy import Column, Integer, String
from database.config.base import Base

class StatusNotebookEntity(Base):
    __tablename__ = 'statusnotebook'
    sta_id = Column(Integer, primary_key=True, autoincrement=True)
    sta_nome = Column(String)