import pandas as pd
import streamlit as st
import plotly.graph_objs as go
import plotly.express as px

#Carregando Dados
df = pd.read_csv("youtube.csv", encoding='latin1')

#Apresentação
st.title("Youtube em Dados")
st.write("Conheça mais informações sobre os 1000 maiores canais do Youtube.")

with st.sidebar:
  filter = st.selectbox("Aplicar filtro", options=["Country", "category", "created_year", "created_month", "Nenhum"], index=4 )
if filter == "Nenhum":
  st.write(df)
else:  
  if filter != "created_year": 
    options = sorted(df[filter].astype(str).unique())
  else:
    options = sorted(df[filter].unique())  
    
  with st.sidebar:
    selected = st.selectbox(f"Selecione o {filter} desejado", options) 
  if filter == "created_year":
    selected = int(selected)

  df_filtered = df[df[filter] == selected].reset_index(drop=True)
  st.write(df_filtered)

st.header("Resumo das informações")
st.write(df.describe())


distribution = st.selectbox("Selecione o tipo de distribuição", ["Absoluta", "Relativa"])

if(distribution == "Absoluta"):
#Distribuição de inscritos por categorias (Absoluto)
  subsByCategory = []
  for category, group in df.groupby('category'):
    subsByCategory.append(
        go.Bar(
            x=[category],
            y=[group['subscribers'].sum()],
            name=category
        )
    )

  layout_sum_subs_by_category = go.Layout(
      title=f"Distribuição de inscritos por categoria.",
      xaxis=dict(title='Categoria'),
      yaxis=dict(title='Soma de Inscritos')
  )
  fig_subsByCategory = go.Figure(data=subsByCategory, layout=layout_sum_subs_by_category)
  st.plotly_chart(fig_subsByCategory)
  
  #Distribuição de views por categorias
  subsByCategory = []
  for category, group in df.groupby('category'):
    subsByCategory.append(
        go.Bar(
            x=[category],
            y=[group['video views'].sum()],
            name=category
        )
    )

  layout_sum_subs_by_category = go.Layout(
      title=f"Soma de views por tipo de canal",
      xaxis=dict(title='Categoria'),
      yaxis=dict(title='Soma de Views')
  )

  fig_subsByCategory = go.Figure(data=subsByCategory, layout=layout_sum_subs_by_category)
  st.plotly_chart(fig_subsByCategory)
  
else:
#Distribuição de inscritos por categorias (Relativo)
  subsByCategoryPie = df.groupby('category')['subscribers'].sum().reset_index()
  fig = px.pie(values=subsByCategoryPie['subscribers'], names=subsByCategoryPie['category'], title='Distribuição de inscritos por categoria.')
  st.plotly_chart(fig)

  viewsByCategory = df.groupby('category')['video views'].sum().reset_index()
  figPieByView = px.pie(values=viewsByCategory['video views'], names=viewsByCategory['category'], title='Distribuição de views por categoria.')
  st.plotly_chart(figPieByView)


#Classificação de views por inscritos
df['views/inscritos'] = df.apply(lambda row: round(row['video views']/row['subscribers'], 1), axis=1)
sortedByViewsSubs = df.sort_values(by='views/inscritos', ascending=False).head(10)

data = [
  go.Bar(
    x=sortedByViewsSubs['Youtuber'].head(10),
    y=sortedByViewsSubs['views/inscritos'].head(10),
  )
]

viewsBySubs_Layout = go.Layout(
    title='10 Canais com a melhor média de views por inscrito.',
    xaxis=dict(title='Canal'),
    yaxis=dict(title='views/inscritos')
)

fig = go.Figure(data=data, layout=viewsBySubs_Layout)
st.plotly_chart(fig)
