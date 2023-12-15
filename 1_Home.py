import pandas as pd
import streamlit as st

st.title("Descrição da Base de Dados")

st.write("Essa base de dados contem informações sobre os maiores canais do Youtube, sobre os quais possui informações e dados importantes como métricas de cada um deles, composta por aproximadamente 1000 linhas. Onde estão disponíveis 28 colunas descritaas a seguir.")

column = ["Rank", "Youtuber", "Subscribers", "Vídeo views", "Category", "Title", "Uploads", "Country", "Abbreviation", "Channel_type", "Vídeo_views_rank", "country_rank", "Channel_type_rank", "Vídeo_views_for_the_last_30_days","Lowest_monthly_earnings", "Highest_monthly_earnings", "Lowest_yearly_earnings", "Highest_yearly_earnings", "Subscribers_for_last_30_days", "Created_year", "Created_month", "Created_date", "Gross tertiary education enrollment (%)", "Population", "Unemployment rate", "Urban_population", "Latitude", "Longitude"]

description = ["Classificação","Nome do canal","Quantidade de inscritos","Número de views que o canal possui","Categoria do canal","Semelhante ao nome do canal","Total de vídeos no canal","País do canal","Sigla do país do canal","Tipo do conteúdo do canal","Classificação pelo número de visualizações","Classificação do canal dentro do país","Classificação dentro do tipo de conteúdo do canal","Total de vídeos nos últimos 30 dias","Ganhos mais baixos em um mês em dólares","Ganhos mais altos em um mês em dólares","Ganhos mais baixos em um ano em dólares","Ganhos mais altos em um ano em dólares","Quantidade de inscritos nos últimos 30 dias","Ano de criação","Mês de criação", "Data exata de criação", "Porcentagem da população matriculada no ensino superior no país", "População do país","Taxa de desemprego do país %", "Taxa da população vivendo em centros urbanos","",""
]

data ={"Título da Coluna": column, "Descrição": description}
df = pd.DataFrame(data)

st.dataframe(df)

st.write("Mais informações sobre a base de dados em: https://www.kaggle.com/datasets/nelgiriyewithana/global-youtube-statistics-2023")
