import pandas as pd

df = pd.read_csv("avgIQpercountry.csv")
df.head()
print(df)

missing_values = df.isnull().sum()
print(missing_values)

import missingno as msno
import matplotlib.pyplot as plt

msno.matrix(df)
plt.show()

msno.bar(df)
plt.show()

msno.heatmap(df)
plt.show()
