import math
# Practicando operaciones básicas
a = 10
b = 3

print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División Entera:", a // b)
print("Potencia:", a ** b)
print("Módulo:", a % b)

# Ejemplos de precedencia de operaciones matemáticas

# Paréntesis tienen la mayor precedencia
expresion1 = (2 + 3) * 5
print("Paréntesis: (2 + 3) * 5 =", expresion1)

# Exponentes
expresion2 = 2 ** 3 * 4
print("Exponentes: 2 ** 3 * 4 =", expresion2)

# Multiplicación y división se evalúan de izquierda a derecha
expresion3 = 16 / 4 * 2
expresion4 = 16 * 2 / 4
print("Multiplicación y división: 16 / 4 * 2 =", expresion3)
print("Multiplicación y división: 16 * 2 / 4 =", expresion4)

# Adición y sustracción se evalúan de izquierda a derecha
expresion5 = 10 - 3 + 2
expresion6 = 10 + 3 - 2
print("Adición y sustracción: 10 - 3 + 2 =", expresion5)
print("Adición y sustracción: 10 + 3 - 2 =", expresion6)

# Combinación de operaciones
expresion7 = (5 + 3) ** 2 - 3 * 2 + 8 / 2
print("Combinada: (5 + 3) ** 2 - 3 * 2 + 8 / 2 =", expresion7)

# Más ejemplos complejos
expresion8 = 2 + 3 * 4 ** 2 / (1 + 1)
print("Compleja: 2 + 3 * 4 ** 2 / (1 + 1) =", expresion8)

c = -14
d = -14
print (c is d)