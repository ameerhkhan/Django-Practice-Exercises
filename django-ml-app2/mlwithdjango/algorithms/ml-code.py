
import json
import  numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
import joblib

df = pd.read_csv('https://raw.githubusercontent.com/pplonski/datasets-for-start/master/adult/data.csv', skipinitialspace=True)
x_cols = [c for c in df.columns if c != 'income']
X = df[x_cols]
y = df['income']


# split to training and testing.
X_train, X_test, y_train, y_test = train_test_split(X, y, testsize=0.3, random_state=1234)

# fill missing values
train_mode = dict(X_train.mode().iloc[0])
X_train = X_train.fillna(train_mode) # replace missing values with the most frequent value.

# Let's convert categoricals to numbers/labels.

encoders = {}

for column in ['workclass', 'education', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'native-country']:
    categorical_convert = LabelEncoder()
    X_train[column] = categorical_convert.fit_transform(X_train[column])
    encoder[column] = categorical_convert

# Our data is now ready to be trained.

rf = RandomForestClassifier(n_estimators=100)
rf = rf.fit(X_train, y_train)

# We will also train ExtraTrees Algorithm

et = ExtraTreesClassifier(n_estimators=100)
et = et.fit(X_train, y_train)

# Now let's save our models.

joblib.dump(train_mode, "./train_mode.joblib", compress=True)
joblib.dump(encoders, "./encoders.joblib", compress=True)
joblib.dump(rf, "./random_forest.joblib", compress=True)
joblib.dump(et, "./extra_trees.joblib", compress=True)




