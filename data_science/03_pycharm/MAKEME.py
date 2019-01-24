import seaborn as sns
import matplotlib.pyplot as plt
from numpy import median
import pandas as pd

diamonds = sns.load_dataset("diamonds")

# 1. Show the distribution of the price variable in a plot

# 2. How many diamonds are there for every different cut type? And show this in a graph

# 3. Show the relation between the `carat` and `price` only for the `fair` diamonds.

# 4. Show the relationship between the `carat` and the `price` for every cut in a different graph

# 5. For every `cut` of diamond calculate the following variables:
#  * minimal `price`
#  * maximal `price`
#  * mean `price`
#  * median `price`

# 6. Show the median price per cut in a graph

# 7. Show in a graph the x and y values of the 10 most expensive and the 10 cheapest diamonds.
# Tip: check the concat, head and tail functions

# 8. show if there is a relation between the color and the price

