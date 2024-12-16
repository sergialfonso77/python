from flask import Flask, request, jsonify
import json
import requests
import os
import platform
from dotenv import load_dotenv

load_dotenv()

OMDB_URL = os.getenv("OMDB_URL")
OMDB_API_KEY = os.getenv("OMDB_API_KEY")
app = Flask(__name__)

PELICULAS_FILE = "peliculas.json"

ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
CIAN = "\033[36m"
RESTABLECER = "\033[0m"

def limpiar_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

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


def guardar_peliculas():
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
        print(ROJO + f"Error al conectar con la API: {e}" + RESTABLECER)
        return None


@app.route('/peliculas', methods=['GET'])
def mostrar_peliculas():
    """Muestra todas las películas en el catálogo."""
    if peliculas:
        return jsonify(peliculas)
    else:
        return jsonify({"message": "No hay películas en el catálogo."}), 404


@app.route('/peliculas', methods=['POST'])
def añadir_pelicula():
    """Añade una nueva película al catálogo."""
    global peliculas  # Añadido para asegurarnos de que modificamos el diccionario global
    peliculas = cargar_peliculas()  # Correcta llamada a la función

    data = request.get_json()
    title = data.get('title')
    año = data.get('año')
    imdbID = data.get("imdbID")

    if title in peliculas:
        return jsonify({"message": f"La película {title} ya está en el catálogo."}), 400

    peliculas[title] = {
        "Year": año,
        "imdbID": imdbID
    }
    guardar_peliculas()
    return jsonify({"message": f"La película {title} ha sido añadida al catálogo."}), 201



@app.route('/peliculas/<nombre>', methods=['DELETE'])
def eliminar_pelicula(nombre):
    """Elimina una película del catálogo."""
    if nombre in peliculas:
        del peliculas[nombre]
        guardar_peliculas()
        return jsonify({"message": f"La película {nombre} ha sido eliminada del catálogo."}), 200
    else:
        return jsonify({"message": f"La película {nombre} no existe en el catálogo."}), 404


@app.route('/peliculas/buscar', methods=['GET'])
def buscar_pelicula():
    """Busca una película en el catálogo por nombre parcial."""
    busqueda = request.args.get('nombre', '').lower()
    coincidencias = [nombre for nombre in peliculas if busqueda in nombre.lower()]
    
    if coincidencias:
        result = {nombre: peliculas[nombre] for nombre in coincidencias}
        return jsonify(result), 200
    else:
        return jsonify({"message": f"No se encontraron películas que coincidan con '{busqueda}'."}), 404


@app.route('/peliculas/presupuesto', methods=['PUT'])
def modificar_presupuesto():
    """Modifica el presupuesto de todas las películas en función de un porcentaje."""
    try:
        porcentaje = float(request.json.get('porcentaje'))
    except (ValueError, TypeError):
        return jsonify({"message": "Por favor, ingresa un valor válido para el porcentaje."}), 400

    for nombre, detalles in peliculas.items():
        try:
            presupuesto_actual = float(detalles["presupuesto"].replace("€", "").replace(",", "").strip())
            nuevo_presupuesto = presupuesto_actual * (1 + porcentaje / 100)

            if nuevo_presupuesto <= 0:
                continue

            detalles["presupuesto"] = f"${nuevo_presupuesto:,.2f}"
        except ValueError:
            continue

    guardar_peliculas()
    return jsonify({"message": f"Los presupuestos han sido modificados en un {porcentaje} %."}), 200


@app.route('/peliculas/sincronizar', methods=['POST'])
def sincronizar_peliculas():
    """Sincroniza las películas desde la API de OMDb."""
    busqueda = request.json.get('busqueda', 'Avatar')
    peliculas_api = obtener_peliculas_api(busqueda)

    if peliculas_api is None:
        return jsonify({"message": "Error al obtener datos de la API o no se encontraron resultados."}), 404

    global peliculas
    peliculas.update(peliculas_api)
    guardar_peliculas()
    return jsonify({"message": f"Películas sincronizadas con la búsqueda '{busqueda}'."}), 200


def mostrar_menu():
    """Muestra el menú interactivo en la terminal."""
    print("\n" + CIAN + "Menú de Gestión de Películas" + RESTABLECER)
    print("1. Mostrar todas las películas")
    print("2. Añadir una nueva película")
    print("3. Eliminar una película")
    print("4. Buscar una película")
    print("5. Modificar presupuesto")
    print("6. Sincronizar películas con la API de OMDb")
    print("7. Salir")
    opcion = input("Elige una opción: ")
    return opcion


def interactuar_con_api():
    """Función que permite interactuar con la API de Flask desde la terminal."""
    while True:
        opcion = mostrar_menu()

        if opcion == '1':
            response = requests.get('http://127.0.0.1:5000/peliculas')
            if response.status_code == 200:
                peliculas = response.json()
                for nombre, detalles in peliculas.items():
                    print(f"{nombre} - Año: {detalles['Year']}, IMDb ID: {detalles['imdbID']}")
            else:
                print("No hay películas en el catálogo.")

        elif opcion == '2':
            title = input("Nombre de la película: ")
            año = input("Año de lanzamiento: ")
            imdbID = input("IMDb ID: ")

            data = {
                'title': title,
                'año': año,
                'imdbID': imdbID
            }
            response = requests.post('http://127.0.0.1:5000/peliculas', json=data)
            print(response.json()["message"])

        elif opcion == '3':
            nombre = input("Nombre de la película a eliminar: ")
            response = requests.delete(f'http://127.0.0.1:5000/peliculas/{nombre}')
            print(response.json()["message"])

        elif opcion == '4':
            busqueda = input("Introduce el nombre de la película a buscar: ")
            response = requests.get(f'http://127.0.0.1:5000/peliculas/buscar?nombre={busqueda}')
            if response.status_code == 200:
                peliculas = response.json()
                for nombre, detalles in peliculas.items():
                    print(f"{nombre} - Año: {detalles['Year']}, IMDb ID: {detalles['imdbID']}")
            else:
                print(response.json()["message"])

        elif opcion == '5':
            porcentaje = input("Introduce el porcentaje de modificación del presupuesto: ")
            data = {'porcentaje': porcentaje}
            response = requests.put('http://127.0.0.1:5000/peliculas/presupuesto', json=data)
            print(response.json()["message"])

        elif opcion == '6':
            busqueda = input("Introduce el término de búsqueda (por defecto 'Avatar'): ")
            data = {'busqueda': busqueda}
            response = requests.post('http://127.0.0.1:5000/peliculas/sincronizar', json=data)
            print(response.json()["message"])

        elif opcion == '7':
            print("Saliendo...")
            break

        else:
            print("Opción no válida. Por favor, elige una opción válida.")


if __name__ == '__main__':
    import threading

    def run_flask_app():
        app.run(debug=True, use_reloader=False)

    flask_thread = threading.Thread(target=run_flask_app)
    flask_thread.start()

    # Luego ejecutamos la interacción por consola
    interactuar_con_api()
