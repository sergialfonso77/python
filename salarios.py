from statistics import mean

# Datos de personas
personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Madrid", "salario": 25000},
    {"nombre": "Juan", "edad": 30, "ciudad": "Sevilla", "salario": 30000},
    {"nombre": "María", "edad": 22, "ciudad": "Madrid", "salario": 22000},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona", "salario": 35000},
]

# Función para obtener el salario de una persona
def get_salary(persona):
    return persona["salario"]

# Crear diccionario de salarios por ciudad
def crear_diccionario_salarios_por_ciudad(personas):
    salarios_por_ciudad = {}
    for persona in personas:
        ciudad = persona["ciudad"]
        salario = persona["salario"]
        if ciudad not in salarios_por_ciudad:
            salarios_por_ciudad[ciudad] = []
        salarios_por_ciudad[ciudad].append(salario)
    return salarios_por_ciudad

# Calcular la media de salarios por ciudad
def calcular_media_salarios_por_ciudad(salarios_por_ciudad):
    return {ciudad: mean(salarios) for ciudad, salarios in salarios_por_ciudad.items()}

# Filtrar personas con salario por encima de la media global
def filtrar_personas_salario_alto(personas, salario_medio_global):
    return list(filter(lambda persona: persona["salario"] > salario_medio_global, personas))

# Filtrar personas con salario por encima de la media de su ciudad
def filtrar_personas_salario_alto_ciudad(personas, media_salarios_por_ciudad):
    return list(filter(lambda persona: persona["salario"] > media_salarios_por_ciudad[persona["ciudad"]], personas))

# Encontrar la persona más joven con el salario más alto
def persona_mas_joven_con_salario_alto(personas):
    return min(personas, key=lambda persona: (-persona["salario"], persona["edad"]))

# Obtener el top 5 de personas más jóvenes con salario más alto
def top_5_personas_jovenes_salario_alto(personas):
    return sorted(personas, key=lambda persona: (-persona["salario"], persona["edad"]))[:5]

# Función principal para ejecutar todas las operaciones
def main():
    salarios_por_ciudad = crear_diccionario_salarios_por_ciudad(personas)
    print("Salarios por ciudad:", salarios_por_ciudad)

    media_salarios_por_ciudad = calcular_media_salarios_por_ciudad(salarios_por_ciudad)
    print("Media de salarios por ciudad:", media_salarios_por_ciudad)

    salario_medio_global = mean(map(get_salary, personas))
    print("Salario medio global:", salario_medio_global)

    personas_con_salario_alto = filtrar_personas_salario_alto(personas, salario_medio_global)
    print("Personas con salario por encima de la media global:")
    for persona in personas_con_salario_alto:
        print(f"{persona['nombre']} - {persona['salario']}")

    personas_con_salario_alto_ciudad = filtrar_personas_salario_alto_ciudad(personas, media_salarios_por_ciudad)
    print("Personas con salario por encima de la media de su ciudad:")
    for persona in personas_con_salario_alto_ciudad:
        print(f"{persona['nombre']} ({persona['ciudad']}) - {persona['salario']}")

    persona_mas_joven = persona_mas_joven_con_salario_alto(personas)
    print("Persona más joven con el salario más alto:", persona_mas_joven)

    top_5_personas = top_5_personas_jovenes_salario_alto(personas)
    print("Top 5 personas más jóvenes con salario más alto:")
    for persona in top_5_personas:
        print(f"{persona['nombre']} - {persona['salario']} - {persona['edad']}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()
