import pandas as pd

df1 = pd.DataFrame(data={'x': [1, 2], 'y': [2, 1], 'b': 'b'})
df2 = pd.DataFrame(data={'x': [1, 3], 'a': 10, 'b': 'a'})
df3 = pd.DataFrame(data={'x': [1, 1, 2], 'y': [1, 2, 3]})
df4 = pd.DataFrame(data={'x': [1, 1, 2], 'z': ['a', 'b', 'a']})

# Join `df1` and `df2` in such a way that the result has 1 row.

df1.merge(df2, on='x')

# Join `df1` and `df2` in such a way that the result has 2 rows.

df1.merge(df2, on='x', how='left')

# Join `df1` and `df2` in such a way that the result has 3 rows.

df1.merge(df2, on='x', how='outer')

# Join `df3` and `df4` and explain what happens

df3.merge(df4, how='left')
