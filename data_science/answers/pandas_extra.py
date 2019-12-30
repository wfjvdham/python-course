import pandas as pd
import numpy as np
import plotly.express as px
import plotly.io as pio

pio.renderers.default = 'firefox'
gapminder = pd.read_csv("data_science/datasets/gapminder.csv")

# Make a plot that shows the relationship between lifeExp, pop and continent in 1957
gapminder_1957 = gapminder[gapminder['year'] == 1957]
fig = px.scatter(gapminder_1957, x='lifeExp', y='pop', color='continent')
fig.show()


# Show the population growth on earth over time. NOTE first convert the pop to millions, otherwise you get an error
gapminder['pop_mlj'] = gapminder['pop'] / 1000000
fig = px.line(gapminder.groupby('year')['pop_mlj'].sum().reset_index(), x='year', y='pop_mlj')
fig.show()

# Show in a graph for the 10 countries with the highest pop for every country the percentage of the world population
# that is living there in 2007
gapminder_2007 = gapminder[gapminder['year'] == 2007]
gapminder_2007_10 = gapminder_2007.sort_values(by=['pop'], ascending=False).head(10)
gapminder_2007_10['perc'] = gapminder_2007_10['pop'] / gapminder_2007_10['pop'].sum() * 100
px.bar(gapminder_2007_10, x='country', y='perc').show()

# Which country had the highest life expectancy in 1952?
gapminder_1952 = gapminder[gapminder['year'] == 1952]
high_life_country = gapminder_1952.sort_values(by='lifeExp', ascending=False).iloc[1, 0]

# Plot the lifeExp over time for that country
px.bar(gapminder[gapminder['country'] == high_life_country], x='year', y='lifeExp').show()

# Show the average life expectancy per continent in a graph.
px.bar(gapminder.groupby('continent')['lifeExp'].mean().reset_index(), x='continent', y='lifeExp').show()

# Calculate the average life expectancy per year and per continent and show in a plot
px.bar(gapminder.groupby(['continent', 'year'])['lifeExp'].mean().reset_index(),
       x='year', y='lifeExp', color='continent', barmode='group').show()

# Create 3 life expectancy groups; low: lifeExp < 50, medium: lifeExp < 65
# and high: the rest. Show in a graph the size of these groups per year.
gapminder['lifeExp_groups'] = pd.cut(gapminder['lifeExp'], [-np.inf, 50, 65, np.inf])
gapminder_groups = gapminder.groupby(['year', 'lifeExp_groups']).size().reset_index(name='n')
fig = px.bar(gapminder_groups, x='year', y='n', color='lifeExp_groups', barmode='group')
fig.show()

# Count the number of countries in a continent and show in a graph
px.bar(gapminder.groupby('continent')['country'].count().reset_index(), x='continent', y='country').show()