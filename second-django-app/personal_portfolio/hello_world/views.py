from django.shortcuts import render

# Create your views here. 
def hello_world(request): # a view function. @1: create views.
    return render(request, 'hello_world.html', {})



