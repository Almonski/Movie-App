from sqlalchemy import Column, Integer, String
from database import Base

# This defines the actual table in the database
class MovieModel(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    director = Column(String)
    year = Column(Integer)