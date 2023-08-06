import streamlit as st

st.title("Las noticias retarder")

jornadaea = {}

for i in range(38):
    jornadaea[i+1] = []


jornada = 1

st.header("Jornada LaLiga EA Sports: " + jornadaea[jornada])
st.subheader('Retarder de la jornada: Maniancra Team')
