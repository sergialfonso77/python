
# Tupla mixta
tupla_mixta = (1, "dos", [3, 4], {5: "cinco"}, (6, 7), 8.0, True, None, {9})

# Convertir la tupla en una lista
mi_lista = list(tupla_mixta)

# Mostrar el resultado
print(tupla_mixta)

mi_lista[1] = "tres"

nueva_tupla = tuple(mi_lista)

print(mi_lista)

tupla_num = (1, 24, 3, 5, 6)

print(sum(tupla_num))
print(max(tupla_num))
print(min(tupla_num))

tupla_cuadrados = tuple(x ** 2 for x in tupla_num)

print(tupla_cuadrados)

mi_tupla = ("Pedro", 25, ["Python", "SQL"], True, 3.14)

nombre, edad, *habilidades, pi = mi_tupla

print("Nombre:", nombre)
print("Edad:", edad)
print("Habilidades:", habilidades)
print("Pi:", pi)

