from sqlalchemy import Column, Integer, String, Float, Boolean
from app.database import Base

class Series(Base):
    __tablename__ = "series"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    location = Column(String, nullable=False)

    description = Column(String, nullable=False)

    price_per_night = Column(Float, nullable=False)

    capacity = Column(Integer, nullable=False)

    image_url = Column(String, nullable=True)

    available = Column(Boolean, default=True)