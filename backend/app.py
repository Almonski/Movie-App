from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # New Import
from database import engine, Base
from routes import movie

Base.metadata.create_all(bind=engine)

app = FastAPI()

# --- CORS Configuration ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # This allows ALL websites to talk to your backend
    allow_credentials=True,
    allow_methods=["*"], # This allows GET, POST, PUT, DELETE, etc.
    allow_headers=["*"], # This allows all headers
)

app.include_router(movie.router, prefix="/movies")