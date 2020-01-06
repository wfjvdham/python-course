import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'firefox'

weather = pd.read_csv("data_science/datasets/weather.csv")

columns = list(weather)
value_vars = [item for item in columns if item.startswith('d')]
id_vars = list(set(columns) - set(value_vars))
weather1 = pd.melt(weather, id_vars=id_vars, value_vars=value_vars)
weather1 = weather1[~np.isnan(weather1['value'])]
weather1['day'] = weather1['variable'].str[1]
del weather1['variable']

weather_per_month = weather1.groupby('month').size().reset_index(name='count')
px.bar(weather_per_month, x='month', y='count').show()

weather_per_month = weather1.groupby(['month', 'element'])['value'].mean().reset_index()
px.bar(weather_per_month, x='month', y='value', color='element', barmode='group').show()

pew = pd.read_csv("data_science/datasets/pew.csv")

columns = list(pew)
id_vars = ['religion']
value_vars = list(set(columns) - set(id_vars))
pew1 = pd.melt(pew, id_vars=id_vars, value_vars=value_vars)

perc = pew1[pew1['variable']=="Don't,know/refused"].groupby('religion')['value'].sum() / \
pew1.groupby('religion')['value'].sum() * 100

px.bar(perc.reset_index().sort_values(by='value'), x='value', y='religion', orientation='h').show()

largest_religions = (pew1
                     .groupby('religion')['value'].sum()
                     .reset_index()
                     .sort_values(by='value', ascending=False).head(3)
                     )

pew_largest_religions = pew1[pew1['religion'].isin(largest_religions['religion'])]

px.bar(pew_largest_religions, x='variable', y='value', color='religion', barmode='group').show()