from api.database import db
from api.models.director import Director

from pymongo.errors import DuplicateKeyError
from fastapi import HTTPException

def listar_directores():
    return list(db.directores.find())

def obtener_director_por_id(id: int):
    return db.directores.find_one({"_id": id})

def agregar_director(director: Director):
    """ 
        Agrega un nuevo director 
        params:
            director: datos a a agregar        
    """
    documento = {
        "_id": director.id,
        "nombre": director.nombre,
        "nacionalidad": director.nacionalidad
    }

    try:
        db.directores.insert_one(documento)

        return {
            "mensaje": "Director agregado correctamente"
        }

    except DuplicateKeyError:
        return None

def actualizar_director(id: int, director: Director):
    documento = {
        "nombre": director.nombre,
        "nacionalidad": director.nacionalidad
    }

    resultado = db.directores.update_one(
        {"_id": id},
        {"$set": documento}
    )

    return resultado    