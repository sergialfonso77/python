import pandas as pd

temperaturas = [15, 17, 16, 14, 18, 20, 22]
precipitaciones = [5, 12, 8, 4, 15, 10, 7]

dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

serie_A = pd.Series(temperaturas, index=dias, name='Temperatura (°C)')
serie_B = pd.Series(precipitaciones, index=dias, name='Precipitación (mm)')


serie_A_slicing = serie_A['Miércoles':'Viernes']
serie_B_slicing = serie_B['Miércoles':'Viernes']

print("Serie A (Temperatura) de Miércoles a Viernes:")
print(serie_A_slicing)
print("\nSerie B (Precipitación) de Miércoles a Viernes:")
print(serie_B_slicing)

combinada = pd.concat([serie_A_slicing, serie_B_slicing], axis=1)
combinada.columns = ['Temperatura (°C)', 'Precipitación (mm)']

print("\nSerie Combinada (Temperatura y Precipitación):")
print(combinada)

combinada['Suma'] = combinada['Temperatura (°C)'] + combinada['Precipitación (mm)']

promedio_temperatura = combinada['Temperatura (°C)'].mean()
promedio_precipitacion = combinada['Precipitación (mm)'].mean()

print("\nSerie Combinada con la Suma de Temperatura y Precipitación:")
print(combinada)
print(f"\nPromedio de Temperatura: {promedio_temperatura:.2f} °C")
print(f"Promedio de Precipitación: {promedio_precipitacion:.2f} mm")
