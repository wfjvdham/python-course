import pandas as pd
import numpy as np
import seaborn as sns

flights = pd.read_csv("data_science/datasets/flights.csv")
airports = pd.read_csv("data_science/datasets/airports.csv")

df = (flights
      .merge(airports, how='left', left_on="dest", right_on="faa")
      .rename({'alt': 'dest_alt'}, axis=1)[['origin', 'dest', 'dest_alt']]
      .merge(airports, how='left', left_on="origin", right_on="faa")[['origin', 'dest', 'dest_alt', 'alt']]
      )

df['alt_diff'] = df['alt'] - df['dest_alt']
df = df[~np.isnan(df['alt_diff'])]

sns.distplot(df['alt_diff'])

data_dictionary = pd.DataFrame(data={'column_name': ['gender', 'gender', 'gender', 'commal1', 'commal1', 'commal1', 'commal1'],
                                     'value': [1, 2, 3, 1, 2, 3, 4],
                                     'description': ['male', 'female', 'unknown', 'yes, now', 'yes, < 5 year', 'yes, > 5 years', 'no']})

data = pd.DataFrame(data={'patient_id': [1, 2, 3, 4, 5, 6, 7, 8],
                          'gender': [1, 2, 3, 1, 2, 3, 1, 2],
                          'commal1': [1, 2, 3, 4, 1, 2, 3, 4]})

(data.melt(id_vars='patient_id', value_vars=['gender', 'commal1'], var_name='column_name')
 .merge(data_dictionary, how='left', on=['value', 'column_name'])
 .pivot(index='patient_id', values='description', columns='column_name')
 )
