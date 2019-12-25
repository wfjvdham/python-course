import plotly.express as px
import pandas as pd

flights = pd.read_csv("data_science/datasets/flights.csv")

# Show in a graph the distribution of the distances of the flights
fig = px.histogram(flights, x='distance', nbins=20)
fig.show()

# Show in a graph number of flights per origin
fig = px.histogram(flights, x='origin')
fig.show()

# Show in a graph the relationship between dep_time and arr_time
fig = px.scatter(flights, x='dep_time', y='arr_time')
fig.show()

# Show in a graph the relationship between dep_delay and origin
fig = px.box(flights, x='origin', y='dep_delay')
fig.show()

# Show in a graph the relationship between arr_delay and dep_delay
fig = px.density_contour(flights, x='arr_delay', y='dep_delay')
fig.show()

# Show in a graph the relationship between air_time, distance and origin
fig = px.scatter(flights, x='air_time', y='distance', color='origin')
fig.show()
