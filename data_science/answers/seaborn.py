import pandas as pd
import seaborn as sns
sns.set()

flights = pd.read_csv("data_science/datasets/flights.csv")

# Show in a graph the distribution of the distances of the flights
sns.distplot(flights['distance'])

# Show in a graph number of flights per origin
sns.countplot(x="origin", data=flights)

# Show in a graph the relationship between dep_time and arr_time
sns.lmplot(x="dep_time", y="arr_time", data=flights)

flights['dep_time_groups'] = pd.cut(flights['dep_time'], 4)
sns.boxplot(x='arr_time', y='dep_time_groups', data=flights)

# Show in a graph the relationship between dep_delay and origin
fig = sns.boxplot(x='dep_delay', y='origin', data=flights)
fig.set(xlim=(-100, 250))

# Show in a graph the relationship between month and origin
sns.countplot(x="origin", hue="month", data=flights)

# Show in a graph the relationship between arr_delay and dep_delay
sns.scatterplot(x="arr_delay", y="dep_delay", data=flights)

flights['dep_delay_groups'] = pd.cut(flights['arr_delay'], 4)
sns.boxplot(x='dep_delay_groups', y='arr_delay', data=flights)

# Show in a graph the relationship between air_time, distance and origin
sns.scatterplot(x='air_time', y='distance', hue='origin', data=flights)

# Show in a graph the relationship between air_time, distance and dep_delay
sns.scatterplot(x='air_time', y='distance', hue='dep_delay', data=flights)
