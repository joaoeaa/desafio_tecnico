from typing import Optional
from pydantic import BaseModel
from datetime import date

class EventBase(BaseModel):
    title: str
    start_date: date
    end_date: Optional[date] = None
    source_agenda: str

class EventCreate(EventBase):
    pass

class Event(EventBase):
    id: int

    class Config:
        from_attributes= True