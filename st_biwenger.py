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

st.sidebar.subheader('Retarders de la jornada')
st.sidebar.image(image, caption='Two guys in the mountain')


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['BuBufas Team', 'Riostra FC', 'Patoto FC'])

st.area_chart(chart_data)