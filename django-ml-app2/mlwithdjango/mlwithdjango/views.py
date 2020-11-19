from django.shortcuts import render
import pandas as pd
import pickle

def home(request):
    return render(request, 'index.html')

def get_class(sep_len, sep_width, pet_len, pet_width):
    # model = pd.read_pickle('Q:/Hamza/Python/django/Django-Practice-Exercises/django-ml-app2/mlwithdjango/mlwithdjango/iris-model.pickle')
    model = pickle.load(open("Q:/Hamza/Python/django/Django-Practice-Exercises/django-ml-app2/mlwithdjango/mlwithdjango/iris-model.sav", "rb"))
    prediction = model.predict([[sep_len, sep_width, pet_len, pet_width]])
    return(prediction)

def result(request):
    sep_len = int(request.GET['sep_len'])
    sep_width = int(request.GET['sep_width'])
    pet_len = int(request.GET['pet_len'])
    pet_width = int(request.GET['pet_width'])

    result = get_class(sep_len, sep_width, pet_len, pet_width)
    result = str(result)
    result = result.strip("[]'")

    return render(request, 'result.html', {'result': result})
