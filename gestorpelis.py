

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




def main(): 
    peliculas = []
    while True: 
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        if opcion == "1": 
            añadir_pelicula(peliculas)
        elif opcion == "2":
            eliminar_pelicula(peliculas)

        else: 
            print("Opcion no valida, vuelvelo a intentar")




if __name__ == "__main__":
    main()