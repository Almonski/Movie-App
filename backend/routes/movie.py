from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

# Import your blueprints and storage rules
from models.movie import MovieModel
from schemas.movie import Movie, MovieCreate
from database import SessionLocal

router = APIRouter()

# Helper function to get a database connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 1. READ ALL (The GET endpoint) - THIS WAS MISSING/MISLABELED
@router.get("/", response_model=List[Movie]) 
def read_movies(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    movies = db.query(MovieModel).offset(skip).limit(limit).all()
    return movies

# 5. READ ONE (The GET by ID endpoint) - Komplettering för godkänt
@router.get("/{movie_id}", response_model=Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    # Vi letar efter filmen med matchande ID
    db_movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    
    # Om filmen inte finns (är None), skicka 404 - detta är kravet för godkänt!
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
        
    return db_movie

# 2. CREATE (The POST endpoint)
@router.post("/", response_model=Movie)
def create_movie(movie: MovieCreate, db: Session = Depends(get_db)):
    db_movie = MovieModel(title=movie.title, director=movie.director, year=movie.year)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

# 3. DELETE (The DELETE endpoint)
@router.delete("/{movie_id}")
def delete_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    db.delete(db_movie)
    db.commit()
    return {"message": f"Movie with ID {movie_id} deleted successfully"}

# 4. UPDATE (The PUT endpoint)
@router.put("/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, movie_update: MovieCreate, db: Session = Depends(get_db)):
    db_movie = db.query(MovieModel).filter(MovieModel.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    
    db_movie.title = movie_update.title
    db_movie.director = movie_update.director
    db_movie.year = movie_update.year
    
    db.commit()
    db.refresh(db_movie)
    return db_movie