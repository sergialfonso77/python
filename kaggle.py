import kagglehub
import pandas as pd
import numpy as np

path = kagglehub.dataset_download("PromptCloudHQ/imdb-data")

df = pd.read_csv(f"{path}/IMDB-Movie-Data.csv")

print(df.head())

columns = ['Title', 'Year', 'Runtime (Minutes)', 'Rating', 'Votes', 'Revenue (Millions)']
df = df[columns]

data = df.to_numpy()

mean_revenue = df['Revenue (Millions)'].mean()
df['Revenue (Millions)'] = df['Revenue (Millions)'].fillna(mean_revenue)

# Calcular la calificación promedio de las películas
average_rating = np.mean(df['Rating'])
print(f"Calificación promedio de las películas: {average_rating}")

# Encontrar la película con la duración más larga
longest_movie = df.loc[df['Runtime (Minutes)'].idxmax()]
print(f"La película con la duración más larga es: {longest_movie['Title']} con {longest_movie['Runtime (Minutes)']} minutos.")

# Determinar el ingreso promedio y la mediana de los ingresos
average_revenue = np.mean(df['Revenue (Millions)'])
print(f"Ingreso promedio de las películas: {average_revenue} millones.")

median_revenue = np.median(df['Revenue (Millions)'])
print(f"Ingreso mediano de las películas: {median_revenue} millones.")

# Manipulación de Datos

# Crear un subconjunto de datos con películas lanzadas en los últimos 10 años
current_year = 2024
df_recent = df[df['Year'] >= current_year - 10]

# Mostrar las primeras filas del subconjunto
print(df_recent.head())

# Calcular el promedio de votos para este subconjunto
average_votes_recent = np.mean(df_recent['Votes'])
print(f"Promedio de votos para películas lanzadas en los últimos 10 años: {average_votes_recent}")

# Correlación

# Evaluar la correlación entre la calificación de IMDb y los ingresos de las películas
correlation = np.corrcoef(df['Rating'], df['Revenue (Millions)'])[0, 1]
print(f"Correlación entre la calificación de IMDb y los ingresos de las películas: {correlation}")

# Representar la correlación con un gráfico de dispersión utilizando Matplotlib
import matplotlib.pyplot as plt

plt.scatter(df['Rating'], df['Revenue (Millions)'], alpha=0.5)
plt.title('Correlación entre Calificación de IMDb y los Ingresos de las Películas')
plt.xlabel('Calificación de IMDb')
plt.ylabel('Ingresos (Millones)')
plt.show()
