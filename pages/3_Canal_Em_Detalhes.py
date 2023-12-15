import pandas as pd
import streamlit as st

#Carregando Dados
df = pd.read_csv("youtube.csv", encoding='latin1')

with st.sidebar:
  filter = st.selectbox("Aplicar filtro por: ", options=["Country", "category", "created_year", "created_month"])

if filter != "created_year": 
  options = sorted(df[filter].astype(str).unique())
else:
  options = sorted(df[filter].unique())  
  
with st.sidebar:
  selected = st.selectbox(f"Selecione o {filter} desejado", options) 
  if filter == "created_year":
    selected = int(selected)

youtubersOptions = df[df[filter] == selected]
youtubersOptions = youtubersOptions['Youtuber']

with st.sidebar:
  youtuber =st.selectbox("Selecione o Youtuber", youtubersOptions)

youtuberData = df[df["Youtuber"] == youtuber]
st.title(f"Canal: *_{youtuber}_*")
st.write(f"Posição no ranking Mundial: {youtuberData['rank'].values[0]}")
st.write(f"Número de inscritos: {youtuberData['subscribers'].values[0]}")
st.write(f"Uploads: {youtuberData['uploads'].values[0]}")
st.write(f"Número de views: {int(youtuberData['video views'].values[0])}")
st.write(f"Média de views por vídeo: {round(int(youtuberData['video views'].values[0]) / youtuberData['uploads'].values[0], 2) }")
st.write(f"Categoria: {youtuberData['category'].values[0]}")
st.write(f"País de origem: {youtuberData['Country'].values[0]}")
st.write(f"Data de criação: {int(youtuberData['created_date'].values[0])} de {youtuberData['created_month'].values[0]} de {int(youtuberData['created_year'].values[0])}")
