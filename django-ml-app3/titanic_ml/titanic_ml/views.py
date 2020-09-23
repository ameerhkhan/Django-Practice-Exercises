# this view is responsible for getting the input from the user.
# as well as generating the output.

# Creating the views as functions.
from django.shortcuts import render
import pickle

# Home page view,
def home(request):
    return render(request,'index.html')


# custom method for generating predictions
# always recommended to create the getPredictions file into a separate file and then import it in views.py
def getPredictions(pclass, sex, age, sibsp, parch, fare, C, Q, S):

    model = pickle.load(open("Q:/Hamza/Python/django/Django-Practice-Exercises/django-ml-app3/titanic_ml/titanic_ml/titanic_ml_model.sav", "rb"))
    scaled = pickle.load(open("Q:/Hamza/Python/django/Django-Practice-Exercises/django-ml-app3/titanic_ml/titanic_ml/scalar.sav", "rb"))
    prediction = model.predict(scaled.transform([[pclass, sex, age, sibsp, parch, fare, C, Q, S]]))

    if prediction == 0:
        return("Not Survived")
    elif prediction == 1:
        return("Survived")
    else:
        return("Error!")
    

# Now the view for our result.
def result(request):
    pclass = int(request.GET['pclass'])
    sex = str(request.GET['sex'])
    if sex == 'male':
        sex = 0
    elif sex == 'female':
        sex = 1
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    embC = int(request.GET['embC'])
    embQ = int(request.GET['embQ'])
    embS = int(request.GET['embS'])

    result = getPredictions(pclass, sex, age, sibsp, parch, fare, embC, embQ, embS)

    return render(request, 'result.html', {'result': result})


