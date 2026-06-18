# Cargar librerías
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Leer datos de csv
car_data = pd.read_csv('vehicles_us.csv')

# Crear encabezado y texto de ayuda
st.title("Relación de datos de carros")
st.write("*Mi primera aplicación🛠️💻*")

# Agregar métricas
st.metric("Carros disponibles", "51,525", None, "red")


# Crear borón para histograma
hist_button = st.button('Construir histograma')

# Crear botón para gráfico de dispersión
disp_button = st.button('Construir gráfico de dispersión')


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

if disp_button:
    st.write(
        'Creación de gráfico de dispersión para el conjunto de datos de anuncios de ventas de coches'
    )
    # Se crea una figura vacía y luego se añade un rastro de scatter
    fig2 = go.Figure(
        data=[go.Scatter(x=car_data['odometer'], y=car_data['price'], mode='markers')])

    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig2.update_layout(title_text='Relación entre Odómetro y Precio')

    # Mostrar el gráfico Plotly
    st.plotly_chart(fig2, use_container_width=True)


# Casilla de verificación para mostrar gráfica de barras de autos por año
car_per_year = st.checkbox('Gráfica de autos por año del modelo')

# Crear una df por cantidad de modelos carros por año
car_per_year_df = car_data['model_year'].value_counts(
).sort_values().reset_index()

# si la casilla de verificación está seleccionada
if car_per_year:
    st.write(
        'Creación de gráfico de barras de la cantidad de carros por año del modelo'
    )
    st.bar_chart(
        car_per_year_df,
        x="model_year",
        y="count",
        use_container_width=True
    )

# Filtro de carros por rango de precios

st.header("Filtro de Precios")

# 1. Extraer rangos mínimos y máximos
min_real_price = int(car_data["price"].min())
max_real_price = int(car_data["price"].max())

# 2. Crear el slider de precios
rango_precios = st.slider(
    "Selecciona el rango de precio ($):",
    min_value=min_real_price,
    max_value=max_real_price,
    value=(min_real_price, max_real_price)  # Por defecto muestra todos
)

# 3. Desempaquetar el rango seleccionado
precio_min, precio_max = rango_precios

# 4. Filtrar de acuerdo al df car_data
# Recuerda usar paréntesis para separar las condiciones correctamente
precios_filtrados = car_data[(car_data["price"] >= precio_min) & (
    car_data["price"] <= precio_max)]

# 5. Mostrar el resultado en Streamlit
st.subheader(f"Productos entre ${precio_min} y ${precio_max}")

if not precios_filtrados.empty:
    st.dataframe(precios_filtrados, use_container_width=True)
else:
    st.warning("Ningún producto coincide con el rango seleccionado.")

st.divider()
st.text('Elaborado por Paulina Serrano\nEstudiante para científica de datos\nCampeche, México\nA 17 de junio de 2026')
