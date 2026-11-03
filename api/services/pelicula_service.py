from api.database import db
from api.models.pelicula import Pelicula
from api.utils.serializer import serializar_lista

from pymongo.errors import DuplicateKeyError

def listar_peliculas():
    """
    Obtiene los documentos
    """
    peliculas = db.peliculas.find()
    return serializar_lista(peliculas)

def filtrar_peliculas(titulo: str):
    peliculas = list(db.peliculas.find({                
                    "titulo": {
                        "$regex": titulo,
                        "$options": "i"
                    }
            }))
    return serializar_lista(peliculas)

def filtrar_por_director(id_director: int):
    resultado = list(db.peliculas.find({"director_id": id_director}))
    return serializar_lista(resultado)

def filtrar_por_anio(anio: int):
    resultado = list(db.peliculas.find({"anio":{"$gte" : anio} }))
    return serializar_lista(resultado)

def agregar_pelicula(pelicula: Pelicula) -> dict:
    """ 
        Agrega una nueva pelicula
        params:
            pelicula: datos a a agregar        
    """
    documento = pelicula.model_dump()
    resultado = db.peliculas.insert_one(documento)
    return {
        "mensaje": "Película agregada correctamente",
        "id": str(resultado.inserted_id)
        }
