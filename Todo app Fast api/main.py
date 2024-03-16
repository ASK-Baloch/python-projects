# main.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Todo as todoo
from pydantic import BaseModel
from typing import Optional


class Todo(BaseModel):

    title: str
    description: str

    class Config:
        from_attributes = True


app = FastAPI()
# Dependency


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/todos/")
def create_todo(todo: Todo, db: Session = Depends(get_db)):

    new_todo = todoo(title=todo.title, description=todo.description)
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return todo


@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo, db: Session = Depends(get_db)):
    new_todo = todoo(title=updated_todo.title,
                     description=updated_todo.description)
    db_todo = db.query(todoo).filter(todoo.id == todo_id).first()

    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in updated_todo.dict().items():
        setattr(db_todo, key, value)
    db.commit()
    return db_todo


@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):

    db_todo = db.query(todoo).filter(todoo.id == todo_id).first()
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(db_todo)
    db.commit()
    return {"message": "Todo deleted"}
