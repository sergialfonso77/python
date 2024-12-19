
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import gradio as gr



df = pd.read_csv('https://drive.google.com/uc?export=download&id=10gsviaZaykZ4D7fwKHERsmVW6Tygqkav')
df_distritos = pd.read_csv('https://drive.google.com/uc?export=download&id=10k2nNfvGUm6do9QMgtR4sd_Q4LGsd1_U')

# X son las características (superficie_construida y distritos_id) e Y es lo que queremos predecir (precio)
x = df[['superficie_construida', 'distritos_id']]
y = df['precio']

df['precio_m2'] = df['precio'] / df['superficie_construida']

df = df[df['precio_m2'] < df['precio_m2'].quantile(0.99)]
df = df[df['precio_m2'] > df['precio_m2'].quantile(0.01)]

# Con los datos limpios volvemos a reasignar x e y
x = df[['superficie_construida', 'distritos_id']]
y = df['precio']

# Normalizar los datos
media_superficie = x['superficie_construida'].mean()
std_superficie = x['superficie_construida'].std()
superficie_normalizada = (df['superficie_construida'] - media_superficie) / std_superficie
# Combinar la superficie normalizada con 'distritos_id' no normalizado
caracteristicas = pd.DataFrame({
'superficie_construida': superficie_normalizada,
'distritos_id': df['distritos_id']
})
precios = (y - y.mean()) / y.std()

# Dividir los datos en conjunto de entrenamiento y prueba
x_train, x_test, y_train, y_test = train_test_split(caracteristicas, precios, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
model = LinearRegression()
# Entrenar el modelo
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'MSE: {mse}')
print(f'R²: {r2}')

distritos = dict(zip( df_distritos['id'],df_distritos['distrito']))
# Crear la lista de opciones para el Dropdown como tuplas (nombre, id)
opciones_distritos = [(nombre, id) for id, nombre in distritos.items()]


def predict_precio(superficie, distrito):
    # Normalizar solo la superficie construida
    superficie_normalizada = (superficie - media_superficie) / std_superficie
    # Convertirlos en un DataFrame de Pandas para la predicción
    datos_prediccion = pd.DataFrame({
    'superficie_construida': [superficie_normalizada],
    'distritos_id': [distrito]
    })
    # Hacer la predicción (sin normalizar el distrito)
    precio_pred_normalizado = model.predict(datos_prediccion)
    # Desnormalizar la predicción del precio para mostrarlo al usuario
    precio_pred = precio_pred_normalizado * y.std() + y.mean()
    precio_formateado = '{:20,d} €'.format(int(precio_pred[0]))
    return precio_formateado


# Crear la interfaz con Gradio
iface = gr.Interface(
    fn=predict_precio,
    inputs=["number", gr.Dropdown(opciones_distritos)],
    outputs="text", # Cambiado a 'text' para permitir una cadena
    title="Predicción de Precio de Inmueble",
    description="Introduce los metros cuadrados y selecciona el distrito para predecir el precio"
)
# Ejecutar la interfaz
iface.launch()