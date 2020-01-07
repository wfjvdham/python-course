- Show in a plot the distribution of the difference in altitude between the `origin` airport and the `dest` airport. You can you the `flights` and the `airports` data frames for that.
- Create the following datasets:

```python
data_dictionary = pd.DataFrame(data={'column_name': ['gender', 'gender', 'gender', 'commal1', 'commal1', 'commal1', 'commal1'],
                                     'value': [1, 2, 3, 1, 2, 3, 4],
                                     'description': ['male', 'female', 'unknown', 'yes, now', 'yes, < 5 year', 'yes, > 5 years', 'no']})

data = pd.DataFrame(data={'patient_id': [1, 2, 3, 4, 5, 6, 7, 8],
                          'gender': [1, 2, 3, 1, 2, 3, 1, 2],
                          'commal1': [1, 2, 3, 4, 1, 2, 3, 4]})
```

- Replace the numeric values in the columns in the `data` with the corresponding descriptions from the `data_dictionary`.