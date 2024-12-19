import kagglehub
import pandas as pd


path = kagglehub.dataset_download("PromptCloudHQ/imdb-data")

df = pd.read_csv(f"{path}/IMDB-Movie-Data.csv")

columns = ['Title', 'Description', 'Genre', 'Director', 'Actors', 'Year', 'Rating', 'Votes', 'Runtime (Minutes)']

df = df[columns]

df['Genre'] = df['Genre'].str.lower().fillna('')
df['Director'] = df['Director'].str.lower().fillna('')
df['Actors'] = df['Actors'].str.lower().fillna('')
df['Description'] = df['Description'].str.lower().fillna('')
