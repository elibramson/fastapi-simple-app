from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional, Annotated
from contextlib import asynccontextmanager
from database import create_tables, delete_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Deleting tables")
    await create_tables()
    print("Creating tables")
    yield
    print("Closing the app")

app = FastAPI(lifespan=lifespan)

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
