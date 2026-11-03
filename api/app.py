from fastapi import FastAPI
from pymongo import MongoClient
import os

from api.routes import (
    directores,
    peliculas
)
tags_metadata = [
    {
        "name": "General",
        "description": "Operaciones generales de la API"
    },
    {
        "name": "Directores",
        "description": "CRUD de directores"
    },
    {
        "name": "Películas",
        "description": "CRUD de películas"
    }
]

app = FastAPI(
    title="API Películas-Directores",
    version="1.0",
    openapi_tags=tags_metadata
)

app.include_router(directores.router)
app.include_router(peliculas.router)

@app.get("/", tags=["General"])
def inicio():
    return {"mensaje": "API Películas-Directores funcionando correctamente"}



