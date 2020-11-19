import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import pickle

# load the dataset
df = pd.read_csv('Q:/Hamza/Python/django/Django-Practice-Exercises/django-ml-app2/mlwithdjango/algorithms/iris.csv')
print(df.head(5))

# split into data and results.
x = df.drop(['species'], axis=1)
y = df['species']

# split into testing and training data.
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)

# Let's train our model.
#%%
model = SVC(gamma='auto')
model.fit(X_train, y_train)


# Predictions?
predictions = model.predict(X_test)
# print(accuracy_score(y_test, predictions))

# pickle the model for usage afterwards in Django.
pd.to_pickle(model, 'Q:/Hamza/Python/django/Django-Practice-Exercises/django-ml-app2/mlwithdjango/algorithms/iris-model.pickle')

# Unpickle the model.
model = pd.read_pickle('Q:/Hamza/Python/django/Django-Practice-Exercises/django-ml-app2/mlwithdjango/algorithms/iris-model.pickle')
pickle.dump(model, open("iris-model.sav", "wb"))
# read a pickle
# model_out = pd.read_pickle('/iris-model.pickle')

sepal_length = float(input("Enter Sepal Length: "))
sepal_width = float(input("Enter Sepal Width: "))
petal_length = float(input("Enter Petal Length: "))
petal_width = float(input("Enter Petal Width: "))

result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
print(result)