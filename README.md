# Cine inteligente: API 

Aplicación de referencia para analizar una plataforma de cine inteligente. La arquitectura separa totalmente la visualización del acceso a datos:

Por ahora:

```text
MongoDB Atlas <--> FastAPI (agregaciones y reglas de negocio) 
```

En la versión futura:

```text
MongoDB Atlas <--> FastAPI (agregaciones y reglas de negocio) <--> Streamlit
```

Streamlit no tiene dependencia de `pymongo`, URI ni credenciales de Atlas: solo consulta la API HTTP. De esta forma se puede reemplazar Streamlit por otra herramienta de BI sin modificar la capa de datos.

## Colecciones

- `directores`: datos de directores.
- `peliculas`: datos de peliculas.

## Estructura del proyecto
proyecto/
│
├── .env                 variables de entorno
├── .env_bdy0101/        entorno virtual (ignorado por Git)
├── api/
│
├── models/
│   ├── director.py
│   └── pelicula.py
│
├── routes/
│   ├── directores.py
│   └── peliculas.py
│
└── services/
    ├── director_service.py
    └── pelicula_service.py 
├── dashboard/
└── docker-compose.yml

## Inicio rápido

Se requiere Python 3.10 o superior.

1. Cree el entorno e instale dependencias:

   ```bash
   python -m venv .env_bdy0101
   source .env_bdy0101/bin/activate
   pip install -r requirements.txt
   ```

2. Copie `.env_example` a `.env` y complete `MONGO_URI`. No suba ese archivo al repositorio.

3. Ejecute la API:

   ```bash
   uvicorn api.app:app --reload --reload-dir api
   ```

La documentación interactiva queda disponible en `http://localhost:8000/docs`.

- 

Todos los endpoints de analítica aceptan `date_from` y `date_to` en formato `YYYY-MM-DD`.
