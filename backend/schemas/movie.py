from pydantic import BaseModel

# What the user sends us (Input)
class MovieBase(BaseModel):
    title: str
    director: str
    year: int

class MovieCreate(MovieBase):
    pass

# What we send back to the user (Output)
class Movie(MovieBase): 
    id: int

    class Config:
        from_attributes = True