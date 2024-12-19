from keras.models import load_model
import numpy as np
from PIL import Image

from images_kaggle import cargar_y_preprocesar_imagen

def predecir_imagen(modelo, ruta_imagen):
    imagen = cargar_y_preprocesar_imagen(ruta_imagen)
    print(f'Imagen cargada desde {ruta_imagen}')
    imagen = np.expand_dims(imagen, axis=0)
    print('Haciendo predicción...')
    prediccion = modelo.predict(imagen)
    if prediccion[0][0] > 0.5:
       print("La imagen es un perro.")
    else:
       print("La imagen es un gato.")

# Load the trained model
modelo = load_model('data\\modelo_cats_vs_dogs.keras')
print('Modelo cargado.')

# Predict on a single image
predecir_imagen(modelo, 'C:\\Users\\Admin\\Downloads\\R.jpg')
