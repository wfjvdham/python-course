import seaborn as sns
import matplotlib.pyplot as plt
from numpy import median
import pandas as pd

diamonds = sns.load_dataset("diamonds")

# 1. Show the distribution of the price variable in a plot

plt.clf()
sns.distplot(diamonds["price"])
plt.show(block=False)

# 2. How many diamonds are there for every different cut type? And show this in a graph

print(diamonds.groupby('cut').size())

plt.clf()
sns.countplot(diamonds['cut'])
plt.show(block=False)

# 3. Show the relation between the `carat` and `price` only for the `fair` diamonds.

fair_diamonds = diamonds[diamonds['cut'] == 'Fair']
plt.clf()
sns.lmplot(x="price", y="carat", data=fair_diamonds)
plt.show(block=False)

# 4. Show the relationship between the `carat` and the `price` for every cut in a different graph

plt.clf()
sns.lmplot(x="price", y="carat", col="cut", data=diamonds)
plt.show(block=False)

# 5. For every `cut` of diamond calculate the following variables:
#  * minimal `price`
#  * maximal `price`
#  * mean `price`
#  * median `price`

print(diamonds.groupby('cut')['price'].agg([('min_price', 'min'),
                                            ('max_price', 'max'),
                                            ('mean_price', 'mean'),
                                            ('median_price', 'median')]))

# 6. Show the median price per cut in a graph
plt.clf()
sns.barplot(x="cut", y="price", estimator=median, data=diamonds)
plt.show(block=False)

# 7. Show in a graph the x and y values of the 10 most expensive and the 10 cheapest diamonds.
# Tip: check the concat, head and tail functions

diamonds.sort_values(by='price')
cheap_diamonds = diamonds.head(10).copy()
cheap_diamonds['price_class'] = 'cheap'
expensive_diamonds = diamonds.tail(10).copy()
expensive_diamonds['price_class'] = 'expensive'

combined = pd.concat([expensive_diamonds, cheap_diamonds], ignore_index=True)

plt.clf()
sns.lmplot(x='x', y='y', hue='price_class', data=combined)
plt.show(block=False)

# 8. show if there is a relation between the color and the price

plt.clf()
sns.boxplot(x='color', y='price', data=diamonds)
plt.show()
