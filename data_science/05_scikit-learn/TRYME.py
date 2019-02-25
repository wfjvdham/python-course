import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

rng = np.random.RandomState(42)
x = 10 * rng.rand(50)
y = 2 * x - 1 + rng.randn(50)

df = pd.DataFrame({'X': x, 'Y': y})
print(df)

#sns.lmplot(x='X', y='Y', data=df, fit_reg=False)
#plt.show()

model = LinearRegression(fit_intercept=True)

model.fit(df['X'].values.reshape(-1, 1),
          df['Y'].values.reshape(-1, 1))
print(model.coef_)
print(model.intercept_)

newx = np.linspace(-1, 11)
df2 = pd.DataFrame({'newx': newx})

df2['newy'] = model.predict(newx.reshape(-1, 1))
print(df2)

fig, ax = plt.subplots()
sns.regplot(x='newx', y='newy', data=df2, fit_reg=False, ax=ax)
sns.regplot(x='X', y='Y', data=df, fit_reg=False, ax=ax)
#plt.show()

# predict tip based on total bill and sex
# https://medium.com/dunder-data/from-pandas-to-scikit-learn-a-new-exciting-workflow-e88e2271ef62

tips = sns.load_dataset('tips')

# create training and test set

from sklearn.model_selection import train_test_split

train, test = train_test_split(tips, test_size=0.2)
print(train.shape)
print(test.shape)

y = train.pop('tip').values

print(train['sex'].value_counts())

# we have two different categories
# Scikit-learn requires its input to be 2 dimensional

print(train['sex'].ndim)
print(type(train['sex']))

sex_train = train[['sex']].copy()

print(sex_train.ndim)
print(type(sex_train))

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse=False)
sex_train_transformed = ohe.fit_transform(sex_train)
print(sex_train_transformed.shape)

# Here we lost the column names...

feature_names = ohe.get_feature_names()
print(feature_names)

# to go back

sex_inv = ohe.inverse_transform(sex_train_transformed)
print(np.array_equal(sex_inv, sex_train.values))

# if you ahve missing values in the train set

sex_train.iloc[0, 0] = np.nan

from sklearn.impute import SimpleImputer
si = SimpleImputer(strategy='constant', fill_value='MISSING')
sex_train_imputed = si.fit_transform(sex_train)

# Now with pipelines

from sklearn.pipeline import Pipeline

si_step = ('si', SimpleImputer(strategy='constant',
                               fill_value='MISSING'))
ohe_step = ('ohe', OneHotEncoder(sparse=False,
                                 handle_unknown='ignore'))
steps = [si_step, ohe_step]
pipe = Pipeline(steps)

sex_train_transformed = pipe.fit_transform(sex_train)
print(sex_train_transformed.shape)

sex_test = test[['sex']].copy()
sex_test_transformed = pipe.transform(sex_test)
print(sex_test_transformed.shape)
