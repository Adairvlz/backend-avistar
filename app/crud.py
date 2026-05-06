from sqlalchemy.orm import Session
from app import models, schemas


def get_all_series(
    db: Session,
    page: int = 1,
    limit: int = 10,
    q: str = None,
    sort: str = "id",
    order: str = "asc"
):

    query = db.query(models.Series)

    # búsqueda
    if q:
        query = query.filter(
            models.Series.name.ilike(f"%{q}%")
        )

    # ordenamiento
    column = getattr(models.Series, sort, models.Series.id)

    if order == "desc":
        query = query.order_by(column.desc())
    else:
        query = query.order_by(column.asc())

    # paginación
    offset = (page - 1) * limit

    query = query.offset(offset).limit(limit)

    return query.all()


def get_series_by_id(db: Session, series_id: int):
    return db.query(models.Series).filter(
        models.Series.id == series_id
    ).first()


def create_series(db: Session, series: schemas.SeriesCreate):

    new_series = models.Series(
        **series.model_dump()
    )

    db.add(new_series)

    db.commit()

    db.refresh(new_series)

    return new_series


def update_series(
    db: Session,
    series_id: int,
    updated_data: schemas.SeriesCreate
):

    series = get_series_by_id(db, series_id)

    if not series:
        return None

    for key, value in updated_data.model_dump().items():
        setattr(series, key, value)

    db.commit()

    db.refresh(series)

    return series


def delete_series(db: Session, series_id: int):

    series = get_series_by_id(db, series_id)

    if not series:
        return None

    db.delete(series)

    db.commit()

    return series

def create_rating(
    db: Session,
    series_id: int,
    rating_data: schemas.RatingCreate
):

    new_rating = models.Rating(
        series_id=series_id,
        **rating_data.model_dump()
    )

    db.add(new_rating)

    db.commit()

    db.refresh(new_rating)

    return new_rating


def get_ratings_by_series(
    db: Session,
    series_id: int
):

    return db.query(models.Rating).filter(
        models.Rating.series_id == series_id
    ).all()