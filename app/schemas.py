from pydantic import BaseModel
from typing import Optional


class SeriesBase(BaseModel):
    name: str
    location: str
    description: str
    price_per_night: float
    capacity: int
    image_url: Optional[str] = None
    available: bool = True


class SeriesCreate(SeriesBase):
    pass


class SeriesResponse(SeriesBase):
    id: int

    class Config:
        from_attributes = True