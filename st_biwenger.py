import streamlit as st

st.title("Las noticias retarder")

jornadaea = {}

for i in range(38):
    jornadaea[i+1] = []


jornada = 1

st.header("Jornada LaLiga EA Sports: 1")

from PIL import Image

image = Image.open('foto.jpeg')

st.subheader('Retarders de la jornada')
st.image(image, caption='Two guys in the mountain')