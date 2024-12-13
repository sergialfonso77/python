from flask import Flask, request, jsonify
import json

app = Flask(__name__)

peliculas = {}

ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
CIAN = "\033[36m"
RESTABLECER = "\033[0m"


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
    data = request.get_json()
    nombre = data.get('nombre')
    director = data.get('director')
    año = data.get('año')
    presupuesto = data.get('presupuesto')

    if nombre in peliculas:
        return jsonify({"message": f"La película {nombre} ya está en el catálogo."}), 400

    peliculas[nombre] = {
        'director': director,
        'año': año,
        'presupuesto': presupuesto
    }
    return jsonify({"message": f"La película {nombre} ha sido añadida al catálogo."}), 201


@app.route('/peliculas/<nombre>', methods=['DELETE'])
def eliminar_pelicula(nombre):
    """Elimina una película del catálogo."""
    if nombre in peliculas:
        del peliculas[nombre]
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

    return jsonify({"message": f"Los presupuestos han sido modificados en un {porcentaje} %."}), 200


if __name__ == '__main__':
    app.run(debug=True)
