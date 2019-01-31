# Exceptions

> Change the normal flow of a program when something 'exceptional' happens

Useful to deal with situations that can not be controlled completely by the program like:

- User input
- File reading

Where you do not want the program to crash.
    
# Structure

```python
a = 3
b = 0

try:
    a/b
except Exception:
    print('This is not allowed')
else:
    print('Success')
```

Or if you want to show the message inside the exception:

```python
a = 3
b = 0

try:
    a/b
except Exception as e:
    print('This is not allowed, because: ', e.args)
else:
    print('Success')
```