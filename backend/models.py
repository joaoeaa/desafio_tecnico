from sqlalchemy import Column, Integer, String, Date
from .database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    start_date = Column(Date)
    end_date = Column(Date, nullable=True)
    source_agenda = Column(String)
