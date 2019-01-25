#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 13:47:09 2019

@author: wim
"""

import pandas as pd
import seaborn as sns

gapminder = pd.read_csv("../datasets/gapminder.csv")

# 1. Which country had the highest life expectancy in **1952**?

gapminder_1952 = gapminder[gapminder['year'] == 1952]
gapminder_1952.sort_values(by="lifeExp", ascending=False)

print(gapminder_1952.iloc[1])

# 2. Make a plot of the life expectancy (`lifeExp`) vs. population (`pop`) in **1952**.

sns.lmplot(x="lifeExp", y="pop", data=gapminder_1952)

# 3. In the previous graph, change the color of the country depending on the continent.

sns.lmplot(x="lifeExp", y="pop", hue="continent", data=gapminder_1952)


# 4. Split the graph into three different groups for different gdp values.
# What are good values to split on?

gapminder_1952['gdp_group'] = pd.cut(gapminder_1952['gdpPercap'], 3)
sns.lmplot(x="lifeExp", y="pop", hue="continent", row="gdp_group", data=gapminder_1952)

# 5. Check if every country has the same number of measurements.

counts = gapminder.groupby('country').size()
print(counts.unique())

# 6. Show the population growth on earth over time.

pop_year = gapminder.groupby('year')['pop'].sum().reset_index()
sns.lineplot(x='year', y='pop', data=pop_year)

# 7. Show the average life expectancy per year per continent in a graph.

life_cont = gapminder.groupby(['continent', 'year'])['lifeExp'].mean().reset_index()
sns.lineplot(x='year', y='lifeExp', hue='continent', data=life_cont)
