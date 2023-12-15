import pandas as pd
import streamlit as st
import plotly.graph_objs as go

#Carregando Dados
df = pd.read_csv("youtube.csv", encoding='latin1')

options = sorted(df['Country'].astype(str).unique())
with st.sidebar:
  country = st.selectbox(f"Selecione o país desejado:", options) 
  
st.title(f"Youtube no(a) {country}")

channels = df[df['Country'] == country]
nChannels = channels.shape[0]
st.write(f"Número de canais entre os 1000 maiores do youtube: {nChannels}")

st.write(f"Maior canal do País: {channels['Youtuber'].values[0]}")

st.write(f"População do país: {int(channels['Population'].values[0])}")

#Gráfico com a quantidade de inscritos dos maiores canais
if(nChannels >= 10):
  top = 10
else:
  top = nChannels
  
categoriesSubs = channels.head(top)['Youtuber']
valuesSubs = channels.head(top)['subscribers']

data = [
    go.Bar(
        x=categoriesSubs,
        y=valuesSubs,
    )
]

layout = go.Layout(
    title=f"Quantidade de inscritos do(s) {top} maiores canais do(a) {country}",
    xaxis=dict(title='Canal'),
    yaxis=dict(title='Inscritos')
)

fig = go.Figure(data=data, layout=layout)
st.plotly_chart(fig)

#Gráfico com quantidade de inscritos por categorias

subsByCategory = []
for category, group in channels.groupby('category'):
  subsByCategory.append(
      go.Bar(
          x=[category],
          y=[group['subscribers'].sum()],
          name=category
      )
  )

layout_sum_subs_by_category = go.Layout(
    title=f"Soma de inscritos por tipo de canal",
    xaxis=dict(title='Categoria'),
    yaxis=dict(title='Soma de Inscritos')
)

fig_subsByCategory = go.Figure(data=subsByCategory, layout=layout_sum_subs_by_category)

st.plotly_chart(fig_subsByCategory)
