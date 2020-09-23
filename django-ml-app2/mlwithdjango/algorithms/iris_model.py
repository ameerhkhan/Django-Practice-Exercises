import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

# load the dataset
df = pd.read_csv('iris.csv')

# split into data and results.
x = df['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
y = df['classification']

# split into testing and training data.
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)

# Let's train our model.
#%%
model = SVC(gama='auto')
model.fit(X_train, y_train)


# Predictions?
predictions = model.predict(X_test)
print(accuracy_score(y_test, predictions))

# pickle the model for usage afterwards in Django.
pd.to_pickle(model, r'Q:/Hamza/Python/django/Django-Practice-Exercises/django-ml-app/iris-model.pickle')

# Unpickle the model.
model = pd.read_pickle(r'Q:/Hamza/Python/django/Django-Practice-Exercises/django-ml-app/iris-model.pickle')

# read a pickle
# model_out = pd.read_pickle('/iris-model.pickle')

sepal_length = float(input("Enter Sepal Length: "))
sepal_width = float(input("Enter Sepal Width: "))
petal_length = float(input("Enter Petal Length: "))
petal_width = float(input("Enter Petal Width: "))

result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
print(result)