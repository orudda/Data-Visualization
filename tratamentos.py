import pandas as pd
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json

NUMBER_VISUALIZATIONS=7
class Vis:
    def __init__(self):
        self.texts=[]

        df_scores = pd.read_csv('archive/spreadspoke_scores.csv')
        df_teams = pd.read_csv('archive/nfl_teams.csv')
        self.df_stadiums = pd.read_csv('archive/nfl_stadiums.csv', encoding = 'latin-1')
        self.df_states = pd.read_json('archive/us-states.json')

        df_analysis = df_scores.merge(self.df_stadiums, left_on = 'stadium', right_on = 'stadium_name')
        df_final = df_analysis[~df_analysis['spread_favorite'].isna()].reset_index(drop = True).copy()
        df_final['total'] = df_final['score_home'] + df_final['score_away']
        dict_teams_corresp = dict(zip(df_teams['team_id'].to_list(), df_teams['team_name'].to_list()))
        df_final['favorite'] = df_final['team_favorite_id'].map(dict_teams_corresp)

        self.df = df_final.copy()
        self.df['outcome'] = self.df.apply(self.categorize_outcome, axis=1)

        self.df['over_under_line'] = pd.to_numeric(self.df['over_under_line'], errors='coerce')   

        self.df['within_7_points'] = self.df.apply(self.within_7_points, axis=1)

        self.df['within_spread'] = self.df.apply(self.within_spread, axis=1)
        self.df['is_huge_favorite'] = self.df.apply(self.isHugeFavorite, axis=1)

    def categorize_outcome(self, row):
        if row['favorite'] == row['team_home']:
            favorite_score = row['score_home']
            underdog_score = row['score_away']
        else:
            favorite_score = row['score_away']
            underdog_score = row['score_home']

        spread_difference = favorite_score - underdog_score

        if spread_difference > 0 and spread_difference < abs(row['spread_favorite']):
            return "Favorito ganha, mas não superando o esperado"
        elif spread_difference >= abs(row['spread_favorite']):
            return "Favorito ganha superando o esperado"
        else:
            return "Azarão ganha"

    
    def isHugeFavorite(self, row):
        if abs(row['spread_favorite']) >= 14.5:
            return True
        else:
            return False
        
    def within_7_points(self,row):
        if abs(row['total'] - row['over_under_line']) <= 3:
            return True
        else:
            return False
        
    

    def within_spread(self, row):
        if row['outcome'] == "favorite won and covered the spread":
            spread_difference = row['score_home'] - row['score_away'] - row['spread_favorite']
        elif row['outcome'] == "underdog won outright":
            spread_difference = row['score_away'] - row['score_home'] + row['spread_favorite']
        else:
            spread_difference = abs(row['score_home'] - row['score_away'])

        if spread_difference <= 3:
            return True
        else:
            return False
        

    def plotVis1(self):

        # Assuming your DataFrame is named 'df'
        grouped_season = self.df.groupby('schedule_season')

        # Count the number of True and False values for the 'within_7_points' and 'within_spread' columns
        count_within_7_points = grouped_season['within_7_points'].value_counts().unstack().fillna(0).reset_index()
        count_within_7_points['ratio'] = count_within_7_points[True] / (count_within_7_points[True] + count_within_7_points[False])
        count_within_7_points = count_within_7_points[count_within_7_points['schedule_season'] >= 1979]
        count_within_spread = grouped_season['within_spread'].value_counts().unstack().fillna(0).reset_index()
        count_within_spread['ratio'] = count_within_spread[True] / (count_within_spread[True] + count_within_spread[False])
        count_within_spread = count_within_spread[count_within_spread['schedule_season'] >= 1979]

        fig = px.bar(count_within_7_points, x = 'schedule_season', y = 'ratio')
        fig.update_layout(title = 'Porcentagem de jogos por temporada em que o total fica dentro de 3 pontos do total projetado.')
        fig.update_xaxes(title='Temporada')
        fig.update_yaxes(title='Porcentagem')
        fig.update_traces(hovertemplate='Temporada: %{x}<br>Porcentagem: %{y:.0%}')
        fig.layout.yaxis.tickformat = ',.0%'
        st.plotly_chart(fig)

    def plotVis2(self):
        grouped_season_outcome = self.df.groupby(['schedule_season', 'outcome']).size().reset_index(name='count')
        grouped_season_outcome = grouped_season_outcome[grouped_season_outcome['schedule_season'] >= 1979]
        # st.dataframe(grouped_season_outcome)
        grouped_season_outcome['percentage'] = grouped_season_outcome.groupby('schedule_season', group_keys=False)['count'].apply(lambda x: x / x.sum())

        fig = px.area(grouped_season_outcome, x='schedule_season', y='percentage', color='outcome', title='Percentage of Outcome by Season')
        
        fig.update_layout(title = 'Porcentagem de resultados por temporada', legend_title = 'Resultado')
        fig.update_xaxes(title='Temporada')
        fig.update_yaxes(title='Porcentagem')
        
        fig.layout.yaxis.tickformat = '.0%'
        st.plotly_chart(fig)

    def plotVis3(self):
        fig = px.histogram(self.df, x = 'spread_favorite', nbins=100, title='Most common spreads in the NFL, 1979 - present')

        fig.update_layout(title = 'Spreads mais comuns na NFL, 1979 - Presente')
        fig.update_xaxes(title='Spread favorito')
        fig.update_yaxes(title='Contagem')
        fig.update_traces(hovertemplate='Spread favorito: %{x}<br>Contagem: %{y}')
        
        
        st.plotly_chart(fig)

    def plotVis4(self):
        test = self.df.groupby(['weather_wind_mph'])['total'].mean().reset_index()
        fig = px.scatter(test, x = 'weather_wind_mph', y = 'total', title = 'Average Total Score by Wind Velocity, Miles per Hour')
        fig.update_layout(yaxis_range=[22, 50])
        
        fig.update_layout(title = 'Pontuação total média por velocidade do vento, milhas por hora')
        fig.update_xaxes(title='Velocidade do vento em mph')
        fig.update_yaxes(title='Total')
        fig.update_traces(hovertemplate='Velocidade do vento em mph: %{x}<br>Total: %{y}')
        
        st.plotly_chart(fig)
    
    def plotVis5(self):
        favorites_per_team = self.df.groupby(['favorite', 'is_huge_favorite'])['is_huge_favorite'].size().reset_index(name='counts')
        favorites_per_team = favorites_per_team[favorites_per_team['is_huge_favorite'] == True]
        fig = px.bar(favorites_per_team, x = 'favorite', y = 'counts', title = 'Number of times each team has been favored by at least two touchdowns, 1979 - present.')
        
        fig.update_layout(title = 'Número de vezes que cada time foi favorecido por pelo menos dois touchdowns, 1979-presente')
        fig.update_xaxes(title='Favorito')
        fig.update_yaxes(title='Contagem')
        
        st.plotly_chart(fig)

    def plotVis6(self):
        favorites_per_team = self.df.groupby(['favorite', 'is_huge_favorite'])['favorite'].size().reset_index(name='counts')
        fig = px.bar(favorites_per_team, x = 'favorite', y = 'counts', title = 'Number of times each team has been the pre-match favorite, 1979 - present.', color = 'is_huge_favorite')
        
        fig.update_layout(title = 'Número de vezes que cada time foi o favorito pré-jogo, 1979-presente', legend_title = 'Grande Favorito')
        fig.update_xaxes(title='Favorito')
        fig.update_yaxes(title='Contagem')

        
        st.plotly_chart(fig)
        
    def plotVis7(self):
        df_stadium = self.df_stadiums['stadium_location']
        print(df_stadium)
        df_stadium = df_stadium.str.split(", ").str[1]
        df_contagem = df_stadium.value_counts().reset_index()
        df_contagem.columns = ['Sigla', 'Total']
        dicionario_contagem = df_contagem.set_index('Sigla')['Total'].to_dict()
        
        properties = []
        for feature in self.df_states['features']:
            feature['properties']['id'] = feature['id']
            feature['properties']['total'] = dicionario_contagem.get(feature['id'], 0)
            properties.append(feature["properties"])
        df = pd.DataFrame(properties)
        df = df.rename(columns={'name': 'Uf', 'id': 'Sigla', 'total': 'Total'})
        
        with open('archive/us-states.json') as data:
            geojson_data = json.load(data)
            
        fig = px.choropleth_mapbox(
            df, # primeiro parâmetro é o dataframe com os dados
            locations = 'Sigla', # coluna do DF que referencia as IDs do mapa
            geojson = geojson_data, # arquivo com os limites dos estados
            color = 'Total', # indicando qual coluna será utilizada para pintar os estados
            mapbox_style = "carto-positron", # estilo do mapa
            center = {'lon':-95, 'lat':39}, # definindo a posição inicial do mapa
            zoom = 2, # definindo o zoom do mapa (número inteiro entre 0 e 20)
            opacity = 0.5, # definindo uma opacidade para a cor do mapa
            hover_name = "Sigla", # nome do hover
            color_continuous_scale = 'reds', # muda a escala de cor
            range_color = [0, df['Total'].max()], # limites do eixo Y
            hover_data=['Uf'],
        )
        fig.update_layout(
            title = "Quantidade de estadios por região",
            coloraxis_colorbar=dict(title='Total estadios por estado')  # Nome personalizado da legenda
        )
        
        st.plotly_chart(fig)


    def readTexts(self):
        filename="texts/text"
        for i in range(NUMBER_VISUALIZATIONS):
            filen=filename+str(i+1)+".txt"
            arquivo = open(filen, 'r', encoding='utf-8')
            self.texts.append(arquivo.read())
            arquivo.close()

