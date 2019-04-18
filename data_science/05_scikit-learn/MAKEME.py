import pandas as pd
import numpy as np

train = pd.read_csv("data_science/datasets/house_prices/train.csv")
train.head()

train.shape

# Remove the target variable from the training set
y = train.pop('SalePrice').values

vc = train['HouseStyle'].value_counts()
vc

# Scikit-Learn must have 2d data

train['HouseStyle'].ndim
train[['HouseStyle']].ndim

hs_train = train[['HouseStyle']].copy()

# We need to encode because Scikit-Learn does not work with strings

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(sparse=False)
hs_train_transformed = ohe.fit_transform(hs_train)
hs_train_transformed.shape

# To get the column names

feature_names = ohe.get_feature_names()
feature_names

# To transform back

hs_inv = ohe.inverse_transform(hs_train_transformed)
np.array_equiv(hs_inv, hs_train)

# the same transformations we must apply to the test set

test = pd.read_csv('data_science/datasets/house_prices/test.csv')
hs_test = test[['HouseStyle']].copy()
hs_test_transformed = ohe.transform(hs_test)
hs_test_transformed

# possible problems

# category only in test set
# add handle_unknown='ignore' to initiation of encoder
# This also solves missing values in the test set

# NA's in the training set MUST be imputed
hs_train = train[['HouseStyle']].copy()
hs_train.iloc[0, 0] = np.nan

from sklearn.impute import SimpleImputer
si = SimpleImputer(strategy='most_frequent')
# si = SimpleImputer(strategy='constant', fill_value='MISSING')
hs_train_imputed = si.fit_transform(hs_train)
hs_train_imputed

# now using a pipeline

from sklearn.pipeline import Pipeline

si_step = ('si', SimpleImputer(strategy='constant',
                               fill_value='MISSING'))
ohe_step = ('ohe', OneHotEncoder(sparse=False,
                                 handle_unknown='ignore'))
steps = [si_step, ohe_step]
pipe = Pipeline(steps)

hs_train = train[['HouseStyle']].copy()
hs_train.iloc[0, 0] = np.nan
hs_transformed = pipe.fit_transform(hs_train)
hs_transformed.shape

# the fit is not necessary for the test set. It was done already for the training
# and stored in the pipe

hs_test = test[['HouseStyle']].copy()
hs_test_transformed = pipe.transform(hs_test)
hs_test_transformed.shape

# also works for multiple columns

string_cols = ['RoofMatl', 'HouseStyle']
string_train = train[string_cols]
string_train.head(3)

string_train_transformed = pipe.fit_transform(string_train)
string_train_transformed.shape

# get the feature names

ohe = pipe.named_steps['ohe']
ohe.get_feature_names()

# apply this transformer to specific columns using columnTransformer

from sklearn.compose import ColumnTransformer

cat_si_step = ('si', SimpleImputer(strategy='constant',
                                   fill_value='MISSING'))
cat_ohe_step = ('ohe', OneHotEncoder(sparse=False,
                                     handle_unknown='ignore'))

cat_steps = [cat_si_step, cat_ohe_step]
cat_pipe = Pipeline(cat_steps)
cat_cols = ['RoofMatl', 'HouseStyle']
cat_transformers = [('cat', cat_pipe, cat_cols)]
ct = ColumnTransformer(transformers=cat_transformers)

X_cat_transformed = ct.fit_transform(train)
X_cat_transformed.shape

X_cat_transformed_test = ct.transform(test)
X_cat_transformed_test.shape

# the feature names are now one level deeper

ct.named_transformers_['cat'].named_steps['ohe'].get_feature_names()

# get the numeric columns using kind

kinds = np.array([dt.kind for dt in train.dtypes])
all_columns = train.columns.values
is_num = kinds != 'O'
num_cols = all_columns[is_num]

# apply a different pipe to numeric transformers

from sklearn.preprocessing import StandardScaler

num_si_step = ('si', SimpleImputer(strategy='median'))
num_ss_step = ('ss', StandardScaler())
num_steps = [num_si_step, num_ss_step]

num_pipe = Pipeline(num_steps)
num_transformers = [('num', num_pipe, num_cols)]

ct = ColumnTransformer(transformers=num_transformers)
X_num_transformed = ct.fit_transform(train)
X_num_transformed.shape

transformers = [('cat', cat_pipe, cat_cols),
                ('num', num_pipe, num_cols)]
ct = ColumnTransformer(transformers=transformers)
X = ct.fit_transform(train)
X.shape

# As the last step apply the model en score on the train set

from sklearn.linear_model import Ridge

ml_pipe = Pipeline([('transform', ct), ('ridge', Ridge())])
ml_pipe.fit(train, y)

ml_pipe.score(train, y)

from sklearn.model_selection import KFold, cross_val_score
kf = KFold(n_splits=5, shuffle=True, random_state=123)
cross_val_score(ml_pipe, train, y, cv=kf).mean()

from sklearn.model_selection import GridSearchCV

#ml_pipe.named_steps['transform'].named_transformers_['num'].named_steps['si'].strategy
param_grid = {
    'transform__num__si__strategy': ['mean', 'median'],
    'ridge__alpha': [.001, 0.1, 1.0, 5, 10, 50, 100, 1000],
}
gs = GridSearchCV(ml_pipe, param_grid, cv=kf)
gs.fit(train, y)
gs.best_params_

gs.best_score_

pd.DataFrame(gs.cv_results_)

# transform year columns to categorical

from sklearn.preprocessing import KBinsDiscretizer
kbd = KBinsDiscretizer(encode='onehot')
year_built_transformed = kbd.fit_transform(train[['YearBuilt']])
year_built_transformed

year_built_transformed.sum(axis=0)

kbd.bin_edges_

# use this transformer in the pipeline and remove id column

year_cols = ['YearBuilt', 'YearRemodAdd', 'GarageYrBlt',
                 'YrSold']
not_year = ~np.isin(num_cols, year_cols + ['Id'])
num_cols2 = num_cols[not_year]

year_si_step = ('si', SimpleImputer(strategy='median'))
year_kbd_step = ('kbd', KBinsDiscretizer(n_bins=5,
                 encode='onehot-dense'))
year_steps = [year_si_step, year_kbd_step]
year_pipe = Pipeline(year_steps)

transformers = [('cat', cat_pipe, cat_cols),
                ('num', num_pipe, num_cols2),
                ('year', year_pipe, year_cols)]

ct = ColumnTransformer(transformers=transformers)
X = ct.fit_transform(train)
X.shape

ml_pipe = Pipeline([('transform', ct), ('ridge', Ridge())])
cross_val_score(ml_pipe, train, y, cv=kf).mean()