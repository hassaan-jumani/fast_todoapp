from fastapi import FastAPI, HTTPException, Depends,Body
from sqlalchemy.orm.session import Session
from database import Session, engine, Todo
from pydantic_practice import Todo_pydantic

app = FastAPI()

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

@app.post("/create")
def create(todo:Todo_pydantic, db:Session = Depends(get_db)):
    todo = Todo(name = todo.name, description = todo.description)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo 



@app.get("/getall")
def create(db:Session = Depends(get_db)):
    todo = db.query(Todo).all()
    return todo

@app.get(f'/get/{id}')
def create(id:int, db:Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == id).first()
    return todo


 





# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", reload=True)