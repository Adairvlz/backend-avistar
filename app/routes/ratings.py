from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.database import get_db
from app import crud
from app import schemas

router = APIRouter(
    tags=["Ratings"]
)


@router.post(
    "/series/{series_id}/rating",
    status_code=status.HTTP_201_CREATED
)
def create_rating(
    series_id: int,
    rating: schemas.RatingCreate,
    db: Session = Depends(get_db)
):

    series = crud.get_series_by_id(db, series_id)

    if not series:
        raise HTTPException(
            status_code=404,
            detail="Hospedaje no encontrado"
        )

    return crud.create_rating(
        db,
        series_id,
        rating
    )


@router.get("/series/{series_id}/rating")
def get_ratings(
    series_id: int,
    db: Session = Depends(get_db)
):

    series = crud.get_series_by_id(db, series_id)

    if not series:
        raise HTTPException(
            status_code=404,
            detail="Hospedaje no encontrado"
        )

    return crud.get_ratings_by_series(
        db,
        series_id
    )