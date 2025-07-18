from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    print("Deleting tables")
    await create_tables()
    print("Creating tables")
    yield
    print("Closing the app")

app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)