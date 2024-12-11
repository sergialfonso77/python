#!/usr/bin/env python3
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
AZUL = "\033[34m"
CIAN = "\033[36m"
RESTABLECER = "\033[0m"

def mostrar_menu(): 
    print(f"\n{AZUL}Gestor de peliculas{RESTABLECER}")
    print(f"{VERDE}1. Añadir pelicula{RESTABLECER}")
    print(f"{VERDE}2. Eliminar pelicula{RESTABLECER}")
    print(f"{VERDE}3. Mostrar todas las peliculas{RESTABLECER}")
    print(f"{VERDE}4. Buscar pelicula{RESTABLECER}")
    print(f"{VERDE}5. Modificar presupuesto{RESTABLECER}")
    print(f"{ROJO}6. Salir{RESTABLECER}")

def añadir_pelicula(peliculas):
    nombre = input("Escribe el nombre de la pelicula: ").strip()
    if nombre in peliculas:
        print(f"La película {nombre} ya está en el catálogo.")
        return
    director = input("Escribe el nombre del director: ").strip()
    año = input("Escribe el año de estreno: ").strip()
    presupuesto = input("Escribe el presupuesto de la película: ").strip()

    peliculas[nombre] = {
        'director': director,
        'año': año,
        'presupuesto': presupuesto
    }
    print(f"La película {nombre} ha sido añadida al catálogo.")

def eliminar_pelicula(peliculas): 
    nombre = input("Escribe el nombre de la pelicula que deseas eliminar").strip()
    if nombre:
        if nombre in peliculas:
            peliculas.remove(nombre)
            print(f"La pelicula {nombre} ha sido eliminada del catalogo")
        else:
            print(f"La pelicula {nombre} no existe en el catalogo")
    else:
        print("Nombre no valido")

def mostrar_peliculas(peliculas):
    if peliculas:
        for nombre, metadatos in peliculas.items():
            print(f"\n{AMARILLO}{nombre}:")
            print(f"  Director: {metadatos['director']}")
            print(f"  Año: {metadatos['año']}")
            print(f"  Presupuesto: {metadatos['presupuesto']}")
    else:
        print("No hay películas en el catálogo.")

def buscar_pelicula(peliculas):
    busqueda = input("Escribe una parte del nombre de la película que deseas buscar: ").strip().lower()
    coincidencias = [nombre for nombre in peliculas if busqueda in nombre.lower()]
    if coincidencias:
        print("Películas encontradas:")
        for nombre in coincidencias:
            print(f"- {nombre}: {peliculas[nombre]}")
    else:
        print(f"No se encontraron películas que coincidan con '{busqueda}'.")

def modificar_presupuesto(peliculas):
    try:
        porcentaje = float(input("Escribe el porcentaje de incremento o disminucion para el presupuesto: ").strip())
    except ValueError:
        print("Por favor, ingresa un valor válido para el porcentaje.")
        return

    for nombre, detalles in peliculas.items():
        presupuesto_actual = float(detalles["presupuesto"].replace("€", "").replace(",", "").strip())
        nuevo_presupuesto = presupuesto_actual * (1 + porcentaje / 100)
        
        if nuevo_presupuesto <= 0:
            print(f"El presupuesto de la película {nombre} no puede reducirse a 0 o menos.")
            continue

        detalles["presupuesto"] = f"${nuevo_presupuesto:,.2f}"
    print(f"Los presupuestos han sido modificados en un {porcentaje}%.")

def main(): 
    peliculas = {}
    while True: 
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1": 
            añadir_pelicula(peliculas)
        elif opcion == "2":
            eliminar_pelicula(peliculas)
        elif opcion == "3":
            mostrar_peliculas(peliculas)
        elif opcion == "4":
            buscar_pelicula(peliculas)
        elif opcion == "5":
            modificar_presupuesto(peliculas)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else: 
            print("Opcion no valida, vuelvelo a intentar")




if __name__ == "__main__":
    main()