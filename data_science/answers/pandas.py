import pandas as pd
import numpy as np

flights = pd.read_csv("data_science/datasets/flights.csv")

# Use describe() to get a quick overview of the dataset
flights.describe()

# Select the columns dep_time, sched_dep_time, dep_delay, arr_time, sched_arr_time
flights[['dep_time', 'sched_dep_time', 'dep_delay', 'sched_arr_time']]

# How many flights are there on 1^th January 2013?
flights_1_jan = flights[(flights['day']==1) &
                        (flights['month']==1)]
flights_1_jan.shape[0]

# What is the largest distance (in km! (miles x 1.6)) between two airports?
# Also give the names of the airports.
flights.sort_values(by=['distance'], ascending=False)
flights['distance_km'] = flights['distance'] * 1.6
flights.loc[1, ['distance_km', 'origin', 'dest']]

# How many different destinations are there?
flights['dest'].unique().size

# Which destination has the fewest flights?
(flights.groupby('dest').size()
 .reset_index(name='counts')
 .sort_values(by=['counts'], ascending=True)).head()

# What is the median of the distance of all the flights with carrier `DL`?
flights.loc[flights['carrier']=='DL', 'distance'].median()

# Which destination had the most flights in January 2013?
flights_jan = flights[flights['month']==1]
(flights_jan
    .groupby('dest')
    .size()
    .reset_index(name='counts')
    .sort_values(by=['counts'], ascending=False)).head()

# What is the median distance and air_time per carrier
flights.groupby('carrier')['distance', 'air_time'].median().reset_index()

# What is the average dep_delay of all flights
flights['dep_delay'].mean()

# What is the percentage of late flights per origin
flights['delayed'] = flights['dep_delay'] > 0
flights_grouped = flights.groupby('origin')['delayed'].agg(['sum', 'count'])
flights_grouped['perc'] = flights_grouped['sum'] / flights_grouped['count'] * 100

# Define 3 types of flights short: distance < 500, medium: distance < 1000,
# long: the rest. Calculate the average airtime per flight type
flights['distance_group'] = np.select(
    [
        flights['distance'].between(0, 500),
        flights['distance'].between(500, 1000)
    ],
    [
        'short',
        'medium'
    ],
    default='long'
)

flights.groupby('distance_group')['air_time'].mean()
