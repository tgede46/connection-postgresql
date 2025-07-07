from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.util.init_db import create_table
from app.db.models import citation_controllers

@asynccontextmanager
async def lifespan(app:FastAPI):
    print("created")
    create_table()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(citation_controllers.router)
