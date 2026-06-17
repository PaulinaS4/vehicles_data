# Cargar librerías
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Leer datos de csv
car_data = pd.read_csv('notebooks/vehicles_us.csv')

# Crear encabezado y texto de ayuda
st.header("Relación de datos de carros")
st.write("*Se está trabajando en el tablero estadístico...🛠️💻*")

# Agregar métricas
st.metric("Carros disponibles", "51,525", None, "red")


# Crear borón para histograma
hist_button = st.button('Construir histograma')


if hist_button:
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)
