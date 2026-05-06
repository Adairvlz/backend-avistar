from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request

from app.database import Base
from app.database import engine

from app.routes import series
from app.routes import ratings

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
app.include_router(ratings.router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    return JSONResponse(
        status_code=400,
        content={
            "error": "Datos inválidos",
            "details": exc.errors()
        }
    )

@app.get("/")
def home():
    return {
        "message": "AVISTAR API funcionando"
    }