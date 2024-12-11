
texto_largo = ["Linea " + str(i+1) for i in range(1000)]

num_bloques = 1000/25
lineas_por_bloque = 25
contador_global = 0
contador = 0

bloque_actual = []
bloques = []

for linea in texto_largo: 
    bloque_actual.append(linea)

    if (len(bloque_actual) == lineas_por_bloque):
        bloques.append(bloque_actual)
        bloque_actual = []
        contador_global += 1
        print(f"\nBloque {contador_global} de {num_bloques}")