import copy

empleados = [
    ["Pedro", ["Python", "SQL"]],
    ["Manolo", ["Java", "C++", "JavaScript"]],
    ["Alejandro", ["HTML", "CSS", "JavaScript"]]
]

empleados_copy = empleados.copy()
empleados_deepcopy = copy.deepcopy(empleados)

empleados_deepcopy[0][1].append("Java")

print("Lista original:", empleados)
print("Copia superficial:", empleados_copy)
print("Copia profunda:", empleados_deepcopy)

