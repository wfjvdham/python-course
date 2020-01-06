import pandas as pd
import numpy as np

weather = pd.read_csv("data_science/datasets/weather.csv")

columns = list(weather)
value_vars = [item for item in columns if item.startswith('d')]
id_vars = list(set(columns) - set(value_vars))
weather1 = pd.melt(weather, id_vars=id_vars, value_vars=value_vars)
weather1 = weather1[~np.isnan(weather1['value'])]
weather1['day'] = weather1['variable'].str[1]
del weather1['variable']

#optional
weather1.pivot_table(index=['id', 'year', 'month', 'day'], values='value', columns='element',
                     aggfunc=np.mean).reset_index()
pew = pd.read_csv("data_science/datasets/pew.csv")

columns = list(pew)
id_vars = ['religion']
value_vars = list(set(columns) - set(id_vars))
pew1 = pd.melt(pew, id_vars=id_vars, value_vars=value_vars)
