from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db
from app import crud
from app import schemas

router = APIRouter(
    prefix="/series",
    tags=["Series"]
)


@router.get("/")
def get_series(db: Session = Depends(get_db)):
    return crud.get_all_series(db)


@router.get("/{series_id}")
def get_series_by_id(
    series_id: int,
    db: Session = Depends(get_db)
):

    series = crud.get_series_by_id(db, series_id)

    if not series:
        raise HTTPException(
            status_code=404,
            detail="Hospedaje no encontrado"
        )

    return series


@router.post("/", status_code=201)
def create_series(
    series: schemas.SeriesCreate,
    db: Session = Depends(get_db)
):
    return crud.create_series(db, series)