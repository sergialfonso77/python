import pandas as pd

df = pd.read_csv('Titanic-Dataset.csv', index_col="PassengerId" )

print(df)

