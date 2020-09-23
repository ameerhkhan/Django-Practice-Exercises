# from,
# https://towardsdatascience.com/creating-a-machine-learning-based-web-application-using-django-5444e0053a09
import pickle
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# load dataset

data = pd.read_csv('train.csv', encoding='latin-1')
data = data.rename(columns=lambda x: x.strip().lower())
data.head()

# clean missing values.
data = data[['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'survived']]
data['sex'] = data['sex'].map({'male': 0, 'female':1})
data['age'] = pd.to_numeric(data['age'], errors='coerce')
data['age'] = data['age'].fillna(np.mean(data['age']))

# dummy variables
embarked_dummies = pd.get_dummies(data['embarked'])
data = pd.concat([data, embarked_dummies], axis=1)
data = data.drop(['embarked'], axis=1)

X = data.drop(['survived'], axis=1)
y = data['survived']

# scaling features
sc = MinMaxScaler(feature_range=(0,1))
X_scaled = sc.fit_transform(X)

# fit model
log_model = LogisticRegression(C=1)
log_model.fit(X_scaled, y)


# saving model as pickle

pickle.dump(log_model, open("titanic_ml_model.sav", "wb"))
pickle.dump(sc, open("scalar.sav", "wb"))