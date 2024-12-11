

def mostrar_menu(): 
    print("\nGestor de peliculas")
    print("1. Añadir pelicula")
    print("2. Eliminar pelicula")
    print("3. Mostrar todas las peliculas")
    print("4. Buscar pelicula")
    print("5. Salir")

def añadir_pelicula(peliculas): 
    nombre = input("Escribe el nombre de la pelicula").strip()
    if nombre:
        peliculas.append(nombre)
        print(f"La pelicula {nombre} ha sido añadida")
    else:
        print("La pelicula no ha podido ser añadida")

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
    for pelicula in peliculas:
        print(f"\n{pelicula}")

def buscar_pelicula(peliculas):
    busqueda = input("Escribe una parte del nombre de la pelicula que deseas buscar: ").strip().lower()
    coincidencias = [pelicula for pelicula in peliculas if busqueda in pelicula.lower()]
    if coincidencias:
        print("Películas encontradas:")
        for pelicula in coincidencias:
            print(f"- {pelicula}")
    else:
        print(f"No se encontraron películas que coincidan con '{busqueda}'")

def main(): 
    peliculas = []
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
            print("Saliendo del programa...")
            break
        else: 
            print("Opcion no valida, vuelvelo a intentar")




if __name__ == "__main__":
    main()