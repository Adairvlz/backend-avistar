from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

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


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
def create_series(
    series: schemas.SeriesCreate,
    db: Session = Depends(get_db)
):

    return crud.create_series(db, series)


@router.put("/{series_id}")
def update_series(
    series_id: int,
    updated_data: schemas.SeriesCreate,
    db: Session = Depends(get_db)
):

    updated_series = crud.update_series(
        db,
        series_id,
        updated_data
    )

    if not updated_series:
        raise HTTPException(
            status_code=404,
            detail="Hospedaje no encontrado"
        )

    return updated_series


@router.delete(
    "/{series_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_series(
    series_id: int,
    db: Session = Depends(get_db)
):

    deleted_series = crud.delete_series(db, series_id)

    if not deleted_series:
        raise HTTPException(
            status_code=404,
            detail="Hospedaje no encontrado"
        )

    return