try:
    with open("mi_archivo.txt", 'r') as archivo:
        print("El archivo ya existe. No se puede continuar.")
        archivo.close()
except FileNotFoundError:
    print("El archivo no existe. Creando un nuevo archivo...")
    with open("mi_archivo.txt", 'w') as archivo:
        archivo.write("Línea 1: Este es un archivo nuevo.\n")
        archivo.write("Línea 2: Python.\n")
        archivo.write("Línea 3: programar.\n")
        archivo.write("Línea 4: manipulación de archivos.\n")
        archivo.write("Línea 5: ¡hola!\n")
        archivo.close()


try:
    archivo = open("mi_archivo.txt", 'r')
    linea = archivo.readline()
    while linea:
        print(f"Línea: {linea.strip()}")
        print(f"Posición del cursor: {archivo.tell()}")
        linea = archivo.readline()
    archivo.close()
except FileNotFoundError:
    print("No se pudo encontrar el archivo.")

archivo = open("mi_archivo.txt", 'w')
archivo.write("Este es un nuevo contenido del archivo después de sobrescribir.\n")
archivo.close()

archivo = open("mi_archivo.txt", 'a+')
archivo.write("Agregando una nueva línea al final del archivo.\n")
archivo.seek(0)
print("Contenido completo del archivo después de agregar una línea:")
print(archivo.read())
archivo.close()

try:
    archivo = open("mi_archivo.txt", 'a')
    archivo.write("Otra línea agregada con modo 'a'.\n")
    archivo.seek(0)
    print("Contenido completo del archivo después de agregar una línea en modo 'a':")
    print(archivo.read())
    archivo.close()
except Exception as e:
    print(f"Error al intentar leer el archivo en modo 'a': {e}")