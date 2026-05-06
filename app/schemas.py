from pydantic import BaseModel, Field
from typing import Optional


class SeriesBase(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    location: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=10, max_length=500)
    price_per_night: float = Field(..., gt=0)
    capacity: int = Field(..., gt=0, le=30)
    image_url: Optional[str] = None
    available: bool = True


class SeriesCreate(SeriesBase):
    pass


class SeriesResponse(SeriesBase):
    id: int

    class Config:
        from_attributes = True

class RatingCreate(BaseModel):
    score: int = Field(..., ge=1, le=5)
    comment: Optional[str] = None


class RatingResponse(RatingCreate):
    id: int
    series_id: int

    class Config:
        from_attributes = True