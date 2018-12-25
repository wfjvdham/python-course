# NumPy

> Numerical Python is a library for storing large numerical arrays in a efficient way and apply operations on them.

- All items in a numpy array have to be the same type

```
import numpy as np
```

## Create Arrays

Integer array:

```
np.array([1, 4, 2, 5, 3])
```

Using the `dtype` attribute you can set the [type](https://docs.scipy.org/doc/numpy/user/basics.types.html).

```
np.array([1, 2, 3, 4], dtype='float32')
```

or 

```
np.array([1, 2, 3, 4], dtype=np.float32)
```

## Multi dimensional Arrays

```
x1 = np.random.randint(10, size=6)  # One-dimensional array
x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array
```

## Usefull Atributes

```
x3.ndim
x3.shape
x3.size

x3.itemsize
x3.nbytes

x3.type
```

## Indexing

`python` starts with 0.

```
x1[0]
```

negative indexes can be used to get a value from the end of the array

```
# get the last item
x1[-1]
```

```
x2[0, 0]
```

## Slicing

```
x[start:stop:step]
```

defaults:
- `start=0`
- `stop *size of dimension*`
- `step=1`

```
x = np.arange(10)
x
```

```
x[:5]  # first five elements
```