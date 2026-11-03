from pydantic import BaseModel

class Pelicula(BaseModel):
    titulo: str
    year: int
    director: int