# Modeling

## Packages

- [Scikit-learn](https://scikit-learn.org/stable/)
- [statsmodels](https://www.statsmodels.org/stable/index.html)

# Scikit-learn

Here the example data is generated

```python
import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(42)
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)
plt.scatter(x, y);
```

## Choose a class 

- linear regression

```python
from sklearn.linear_model import LinearRegression
```
- random forrest

```python
from sklearn.ensemble import RandomForestClassifier
```
- ...

## Instantiate a model

Parameters of the model are set before the actual fitting of the model

```python
model = LinearRegression(fit_intercept=True)
model
```

In this step there is no computation, only storing the values given.

## Prepare the data

Scikit-learn only accepts 2-dimensional array as input, no `DataFrame`

```python
X = x[:, np.newaxis]
```

## Fit the model

Here the actual computation of the parameters that best fit the data happens.

```python
model.fit(X, y)
```

The results are stored in the model object

```python
model.coef_
model.intercept_
```

## Use the Model to make Predictions

```python
xfit = np.linspace(-1, 11)
Xfit = xfit[:, np.newaxis]

yfit = model.predict(Xfit)

plt.scatter(x, y)
plt.plot(xfit, yfit);
```

## Model Validation

> You cannot accurately validate your model on the same data where you trained your model.

One solution is to keep a separate data set for validating your model (*Validation Set*)

```python
from sklearn.model_selection import train_test_split
from sklearn.metrics import explained_variance_score

# split the data with 50% in each set
X1, X2, y1, y2 = train_test_split(X, y, random_state=0,
                                  train_size=0.5)

# fit the model on one set of data
model.fit(X1, y1)

# evaluate the model on the second set of data
y2_model = model.predict(X2)
explained_variance_score(y2, y2_model)
```

Downside is that the data in the *validation set* is not used for training your model. A better way:

### Cross-Validation

![k fold cv](./k_fold_cv.jpg")

[Documentation](https://scikit-learn.org/stable/modules/cross_validation.html)

```python
from sklearn.model_selection import cross_val_score
cross_val_score(model, X, y, cv=5)
```
