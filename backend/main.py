from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import engine
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/events/", response_model=schemas.Event)
def create_event(event: schemas.EventCreate, db: Session = Depends(get_db)):
    db_event = models.Event(**event.model_dump())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event

@app.get("/events/", response_model=List[schemas.Event])
def read_events(skip: int=0, limit: int=100, db: Session = Depends(get_db)):
    events = db.query(models.Event).offset(skip).limit(limit).all()
    return events
