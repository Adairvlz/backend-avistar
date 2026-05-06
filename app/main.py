from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base
from app.database import engine

from app.routes import series

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AVISTAR API",
    description="API REST para gestionar hospedajes de AVISTAR",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(series.router)

@app.get("/")
def home():
    return {
        "message": "AVISTAR API funcionando"
    }