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
from sklearn.cross_validation import train_test_split
# split the data with 50% in each set
X1, X2, y1, y2 = train_test_split(X, y, random_state=0,
                                  train_size=0.5)

# fit the model on one set of data
model.fit(X1, y1)

# evaluate the model on the second set of data
y2_model = model.predict(X2)
accuracy_score(y2, y2_model)
```

Downside is that the data in the *validation set* is not used for training your model. A better way:

### Cross-Validation

![k fold cv](./k_fold_cv.jpg")

[Documentation](https://scikit-learn.org/stable/modules/cross_validation.html)

```python
from sklearn.cross_validation import cross_val_score
cross_val_score(model, X, y, cv=5)
```

### Learning Curve

> A learning curve shows you if you should add more data or increase the complexity of the model

```python
from sklearn.learning_curve import learning_curve

fig, ax = plt.subplots(1, 2, figsize=(16, 6))
fig.subplots_adjust(left=0.0625, right=0.95, wspace=0.1)

for i, degree in enumerate([2, 9]):
    N, train_lc, val_lc = learning_curve(PolynomialRegression(degree),
                                         X, y, cv=7,
                                         train_sizes=np.linspace(0.3, 1, 25))

    ax[i].plot(N, np.mean(train_lc, 1), color='blue', label='training score')
    ax[i].plot(N, np.mean(val_lc, 1), color='red', label='validation score')
    ax[i].hlines(np.mean([train_lc[-1], val_lc[-1]]), N[0], N[-1],
                 color='gray', linestyle='dashed')

    ax[i].set_ylim(0, 1)
    ax[i].set_xlim(N[0], N[-1])
    ax[i].set_xlabel('training size')
    ax[i].set_ylabel('score')
    ax[i].set_title('degree = {0}'.format(degree), size=14)
    ax[i].legend(loc='best')
```