from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, Annotated

app = FastAPI()

class Task(BaseModel):
    name: str
    description: Optional[str] = None

class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id: int

tasks = []

@app.post("/tasks")
async def add_task(task: Annotated[STaskAdd, Depends()]):
    
    tasks.append(task)
    return {"data": task}
