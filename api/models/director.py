from pydantic import BaseModel
class Director(BaseModel):
    id: int
    nacionalidad: str
    nombre: str