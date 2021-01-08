# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px
from Code.graph import anova
from Code.utils_mail import utils


import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df_mail = utils.get_df_from_csv(10)#TODO mieux presentr le tableau
df_anova = anova.load_data()

fig = anova.box_plot(df_anova)
presentation_site = '''
# Présentation du projet
Cette page présente ce que nous avons réalisé ddurant notre projet DataScience
...
'''
presentation_donnee = '''
## Présentation des donnés
Ici un extrait des données de base que nous disposions : 
'''

app.layout = html.Div(children=[
    dcc.Markdown(children=presentation_site),
    html.Div(children='''
            Dash: A web application framework for Python.
         ''',
             ),
    dcc.Markdown(children=presentation_donnee),
    html.Div(children=dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df_mail.columns],
        data=df_mail.to_dict('records'),
    )),

    html.Div([
        dcc.Graph(
            id='example-graph',
            figure=fig
        ),
        dcc.Slider(
            id='my-slider',
            min=0,
            max=20,
            step=0.5,
            value=10,
        ),
        html.Div(id='slider-output-container')
    ])
])
if __name__ == '__main__':
    app.run_server(debug=True)