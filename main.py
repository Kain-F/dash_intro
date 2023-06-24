import os
import datetime

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input,Output

print(f'{os.getcwd()} -- {datetime.datetime.now()}\n')

# ----------------------------------------------------------------------------------------------------------------------
# initialize app

app = dash.Dash()


# ----------------------------------------------------------------------------------------------------------------------
# import and clean data

df = pd.read_csv('intro_bees.csv')
df = df.groupby(['State','ANSI','Affected by','Year','state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
print(df.head())

# ----------------------------------------------------------------------------------------------------------------------
# app layout
