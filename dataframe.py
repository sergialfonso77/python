import pandas as pd

df = pd.read_csv('pesos_alturas.csv')

print("Primeras 5 filas:")
print(df.head())
print("\nÚltimas 5 filas:")
print(df.tail())

print("\nInformación general del DataFrame:")
print(df.info())

print("\nEstadísticas descriptivas básicas:")
print(df.describe())

df['Altura_cm'] = df['Altura_in'] * 2.54

df['Peso_kg'] = df['Peso_lb'] * 0.453592

print("\nValores faltantes en cada columna:")
print(df.isnull().sum())

df = df.dropna()

percentiles_por_genero = df.groupby('Genero')['Peso_kg'].quantile([0.25, 0.5, 0.75])
print("\nPercentiles del peso por género (25%, 50%, 75%):")
print(percentiles_por_genero)

df['IMC'] = df['Peso_kg'] / (df['Altura_cm'] / 100) ** 2

def clasificar_imc(imc):
    if imc < 18.5:
        return 'Bajo Peso'
    elif 18.5 <= imc < 24.9:
        return 'Peso Normal'
    elif 25 <= imc < 29.9:
        return 'Sobrepeso'
    else:
        return 'Obesidad'

df['Clasificación_IMC'] = df['IMC'].apply(clasificar_imc)

print("\nPrimeros registros con clasificación por IMC:")
print(df[['Genero', 'Altura_cm', 'Peso_kg', 'IMC', 'Clasificación_IMC']].head())

df.to_csv('resultado_analisis.csv', index=False)
print("\nResultados guardados en 'resultado_analisis.csv'.")

