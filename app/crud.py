from sqlalchemy.orm import Session
from app import models, schemas


def get_all_series(db: Session):
    return db.query(models.Series).all()


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