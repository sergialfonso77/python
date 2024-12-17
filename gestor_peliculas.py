from fastapi import FastAPI, HTTPException
from pydantic import ValidationError
from typing import List, Dict
import json
import requests
import os
from models import Pelicula
from dotenv import load_dotenv

load_dotenv()

OMDB_URL = os.getenv("OMDB_URL")
OMDB_API_KEY = os.getenv("OMDB_API_KEY")

app = FastAPI()

PELICULAS_FILE = "peliculas.json"

def cargar_peliculas():
    """Carga las películas desde el archivo JSON."""
    if os.path.exists(PELICULAS_FILE):
        with open(PELICULAS_FILE, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    else:
        return {}

def guardar_peliculas(peliculas):
    """Guarda las películas en el archivo JSON."""
    with open(PELICULAS_FILE, 'w', encoding='utf-8') as f:
        json.dump(peliculas, f, ensure_ascii=False, indent=4)

peliculas = cargar_peliculas()

def obtener_peliculas_api(busqueda="Avatar"):
    """Obtiene películas de la API de OMDb."""
    url = f"{OMDB_URL}?apikey={OMDB_API_KEY}&s={busqueda}"
    try:
        response = requests.get(url)
        response.raise_for_status()  
        data = response.json()

        if "Search" in data:
            return {pelicula["Title"]: {
                "Year": pelicula["Year"],
                "imdbID": pelicula["imdbID"]
            } for pelicula in data["Search"]}
        else:
            return None
    except requests.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None


@app.get("/peliculas", response_model=Dict[str, Dict[str, str]])
async def mostrar_peliculas():
    """Muestra todas las películas en el catálogo."""
    if peliculas:
        return peliculas
    else:
        raise HTTPException(status_code=404, detail="No hay películas en el catálogo.")


@app.post("/peliculas", response_model=Dict[str, str])
async def añadir_pelicula(pelicula: Pelicula):
    """Añade una nueva película al catálogo."""
    global peliculas
    peliculas = cargar_peliculas()

    title = pelicula.title
    año = pelicula.año
    imdbID = pelicula.imdbID

    peliculas[title] = {
        "Year": año,
        "imdbID": imdbID
    }
    guardar_peliculas(peliculas)
    return {"message": f"La película {title} ha sido añadida al catálogo."}


@app.delete("/peliculas/{title}", response_model=Dict[str, str])
async def eliminar_pelicula(title: str):
    """Elimina una película del catálogo."""
    global peliculas
    if title in peliculas:
        del peliculas[title]
        guardar_peliculas(peliculas)
        return {"message": f"La película {title} ha sido eliminada del catálogo."}
    else:
        raise HTTPException(status_code=404, detail=f"La película {title} no existe en el catálogo.")


@app.get("/peliculas/buscar", response_model=Dict[str, Dict[str, str]])
async def buscar_pelicula(title: str):
    """Busca una película en el catálogo por title parcial."""
    busqueda = title.lower()
    coincidencias = {title: detalles for title, detalles in peliculas.items() if busqueda in title.lower()}
    
    if coincidencias:
        return coincidencias
    else:
        raise HTTPException(status_code=404, detail=f"No se encontraron películas que coincidan con '{busqueda}'.")


@app.put("/peliculas/presupuesto", response_model=Dict[str, str])
async def modificar_presupuesto(porcentaje: float):
    """Modifica el presupuesto de todas las películas en función de un porcentaje."""
    global peliculas
    for title, detalles in peliculas.items():
        try:
            presupuesto_actual = detalles.get("presupuesto")
            if presupuesto_actual:
                presupuesto_actual = float(presupuesto_actual.replace("€", "").replace(",", "").strip())
                nuevo_presupuesto = presupuesto_actual * (1 + porcentaje / 100)

                if nuevo_presupuesto > 0:
                    detalles["presupuesto"] = f"${nuevo_presupuesto:,.2f}"
        except (ValueError, TypeError):
            continue

    guardar_peliculas(peliculas)
    return {"message": f"Los presupuestos han sido modificados en un {porcentaje} %."}


@app.post("/peliculas/sincronizar", response_model=Dict[str, str])
async def sincronizar_peliculas(busqueda: str = "Avatar"):
    """Sincroniza las películas desde la API de OMDb."""
    peliculas_api = obtener_peliculas_api(busqueda)

    if peliculas_api is None:
        raise HTTPException(status_code=404, detail="Error al obtener datos de la API o no se encontraron resultados.")

    global peliculas
    peliculas.update(peliculas_api)
    guardar_peliculas(peliculas)
    return {"message": f"Películas sincronizadas con la búsqueda '{busqueda}'."}

