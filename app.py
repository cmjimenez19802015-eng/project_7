import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Analisis vehiculos')
car_data= pd.read_csv(r'C:\Users\Home\Documents\repositorios\project_7\vehicles_us.csv')
# Botones para seleccionar los gráficos
scatter_price_model = st.button('Gráfico de Precio vs Modelo')
scatter_price_year = st.button('Gráfico de Precio vs Año del Modelo')

if scatter_price_model:
    st.write('Gráfico de Precio vs Modelo')
    fig = px.scatter(car_data, x="model", y="price", title="Precio por Modelo")
    st.plotly_chart(fig, use_container_width=True)

if scatter_price_year:
    st.write('Gráfico de Precio vs Año del Modelo')
    fig = px.scatter(car_data, x="model_year", y="price", title="Precio por Año del Modelo")
    st.plotly_chart(fig, use_container_width=True)
  # Selector para filtrar por tipo
vehicle_type = st.selectbox('Selecciona el tipo de vehículo', car_data['type'].unique())

# Filtrar los datos según el tipo seleccionado
filtered_data = car_data[car_data['type'] == vehicle_type]

if st.button('Gráfico de Precio vs Modelo Filtrado'):
    st.write(f'Gráfico de Precio vs Modelo para vehículos de tipo: {vehicle_type}')
    fig = px.scatter(filtered_data, x="model", y="price", title=f"Precio por Modelo ({vehicle_type})")
    st.plotly_chart(fig, use_container_width=True)  