import kagglehub
import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import requests

OMDB_API_KEY = "520a2baf"

def obtener_cartel_pelicula(titulo):
    """Función para obtener la URL del cartel de la película desde OMDb API."""
    url = f"http://www.omdbapi.com/?t={titulo}&apikey={OMDB_API_KEY}"
    response = requests.get(url)
    data = response.json()
    
    if data["Response"] == "True":
        return data.get("Poster", None)
    else:
        return None
        
def cargar_datos():
    """Función para cargar el dataset desde Kaggle."""
    path = kagglehub.dataset_download("PromptCloudHQ/imdb-data")
    df = pd.read_csv(f"{path}/IMDB-Movie-Data.csv")
    
    columns = ['Title', 'Description', 'Genre', 'Director', 'Actors', 'Year', 'Rating', 'Votes', 'Runtime (Minutes)', 'Revenue (Millions)', 'Metascore']
    df = df[columns]
    
    return df

def preprocesar_datos(df):
    """Función para preprocesar el dataframe."""
    df['Genre'] = df['Genre'].str.lower().fillna('')
    df['Director'] = df['Director'].str.lower().fillna('')
    df['Actors'] = df['Actors'].str.lower().fillna('')
    df['Description'] = df['Description'].str.lower().fillna('')

    df['Metascore'] = pd.to_numeric(df['Metascore'], errors='coerce')
    df['Revenue (Millions)'] = pd.to_numeric(df['Revenue (Millions)'], errors='coerce')

    df['Metascore'] = df['Metascore'].fillna(df['Metascore'].median())
    df['Revenue (Millions)'] = df['Revenue (Millions)'].fillna(df['Revenue (Millions)'].median())

    return df

def clean_text(text):
    """Función para limpiar el texto eliminando caracteres no alfabéticos."""
    return re.sub(r'[^a-zA-Z\s]', '', text)

def procesar_columnas(df):
    """Función para aplicar la limpieza de texto a las columnas relevantes."""
    df['Genre'] = df['Genre'].apply(clean_text)
    df['Director'] = df['Director'].apply(clean_text)
    df['Actors'] = df['Actors'].apply(clean_text)
    df['Description'] = df['Description'].apply(clean_text)

def crear_columna_combinada(df):
    """Función para crear la columna 'combined_features'."""
    df['combined_features'] = df['Genre'] + ' ' + df['Description'] + ' ' + df['Director'] + ' ' + df['Actors']

def calcular_similitud(df):
    """Función para calcular la matriz de similitud coseno usando TfidfVectorizer."""
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['combined_features'])
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

def obtener_recomendaciones(title, cosine_sim, df):
    """Función para obtener recomendaciones basadas en la similitud coseno."""
    title = title.strip().lower()
    
    try:
        idx = df[df['Title'].str.lower().str.strip() == title].index[0]
    except IndexError:
        return f"Lo siento, no encontramos la película '{title}' en la base de datos. Por favor, revisa el título e intenta de nuevo."

    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    movie_indices = [i[0] for i in sim_scores]

    return df['Title'].iloc[movie_indices]

def interfaz_streamlit(df, cosine_sim):
    """Función que configura la interfaz de usuario con Streamlit."""
    st.title('Sistema de Recomendación de Películas')

    search_query = st.text_input("Empieza a escribir el título de una película que hayas visto:")

    if search_query:
        filtered_movies = df[df['Title'].str.contains(search_query, case=False, na=False)]['Title'].tolist()

        if filtered_movies:
            watched_movie = st.selectbox("Selecciona una película de la lista:", filtered_movies)

            if watched_movie:
                st.write(f"Películas similares a '{watched_movie}':")

                recommendations = obtener_recomendaciones(watched_movie, cosine_sim, df)

                if isinstance(recommendations, str):
                    st.write(recommendations) 
                else:
                    for title in recommendations:
                        movie = df[df['Title'] == title].iloc[0]

                        poster_url = obtener_cartel_pelicula(movie['Title'])
                        
                        st.write(f"**{movie['Title']}** ({movie['Year']}) - Género: {movie['Genre']} - Calificación: {movie['Rating']}")
                        st.write(f"Sinopsis: {movie['Description'][:200]}...")

                        if poster_url:
                            st.image(poster_url, caption=f"Cartel de {movie['Title']}", use_container_width=True)
                        else:
                            st.write("No se pudo obtener el cartel.")
                        
                        st.write("---")
        else:
            st.write("No se encontraron coincidencias con tu búsqueda.")


def main():
    """Función principal que organiza el flujo de la aplicación."""
    df = cargar_datos()
    df = preprocesar_datos(df)
    procesar_columnas(df)
    crear_columna_combinada(df)
    cosine_sim = calcular_similitud(df)
    
    interfaz_streamlit(df, cosine_sim)

if __name__ == "__main__":
    main()
