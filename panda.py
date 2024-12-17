import pandas as pd

numeros = [10, 20, 30, 40, 50]
serie = pd.Series(numeros)

print("Serie Original:")
print(serie)

nuevo_elemento = pd.Series([60])
serie = pd.concat([serie, nuevo_elemento], ignore_index=True)
print("\nSerie después de agregar el elemento 60:")
print(serie)

serie = serie.drop(0).reset_index(drop=True)
print("\nSerie después de eliminar el primer elemento (índice 0):")
print(serie)

suma = serie + 10
print("\nSerie después de sumar 10 a cada elemento:")
print(suma)

resta = serie - 5
print("\nSerie después de restar 5 a cada elemento:")
print(resta)

multiplicacion = serie * 2
print("\nSerie después de multiplicar por 2 a cada elemento:")
print(multiplicacion)

division = serie / 5
print("\nSerie después de dividir entre 5 a cada elemento:")
print(division)
