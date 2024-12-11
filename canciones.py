import random

canciones = ["Song A", "Song B", "Song C", "Song D", "Song E"]
duraciones = [3.5, 4.2, 2.8, 5.0, 3.9]  

canciones_dict = dict(zip(canciones, duraciones))
print("Diccionario combinado:")
print(canciones_dict)

canciones_ordenadas = sorted(canciones_dict.items(), key=lambda x: x[1], reverse=True)
print("\nLas 3 canciones más largas:")
top_3_canciones = dict(canciones_ordenadas[:3])
print(top_3_canciones)

cantidad = 2
canciones_aleatorias = random.sample(list(canciones_dict.items()), cantidad)
print(f"\n{cantidad} canciones seleccionadas aleatoriamente:")
print(dict(canciones_aleatorias))
