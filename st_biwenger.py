import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


st.title("Las noticias retarder")

jornadaea = {}

for i in range(38):
    jornadaea[i+1] = []


jornada = 1

st.header("Jornada LaLiga EA Sports: 1")



image = Image.open('foto.jpeg')

st.subheader('Retarders de la jornada')
st.image(image, caption='Two guys in the mountain')


st.write('\n')
st.write('\n')
st.write('Pajas diarias en las últimas dos semanas')
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['O Carallo', 'Riostra FC', 'Patoto FC'])

st.area_chart(chart_data)

st.write('\n')
st.write('\n')
st.write('Mocha acumulada')
chart_data2 = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['Tomorrowlanders', 'Black Mochamba', 'La Ramallowsky'])

st.line_chart(chart_data2)