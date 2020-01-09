- Create some dummy datasets using the following code

```python
df1 = pd.DataFrame(data={'x': [1, 2], 'y': [2, 1], 'b': 'b'})
df2 = pd.DataFrame(data={'x': [1, 3], 'a': 10, 'b': 'a'})
df3 = pd.DataFrame(data={'x': [1, 1, 2], 'y': [1, 2, 3]})
df4 = pd.DataFrame(data={'x': [1, 1, 2], 'z': ['a', 'b', 'a']})
```

- Join `df1` and `df2` in such a way that the result has 1 row.
- Join `df1` and `df2` in such a way that the result has 2 rows.
- Join `df1` and `df2` in such a way that the result has 3 rows.
- Join `df3` and `df4` and explain what happens
