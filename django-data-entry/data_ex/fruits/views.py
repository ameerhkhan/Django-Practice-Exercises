from django import http
from django.shortcuts import render
from django.http import HttpResponse, response
from .models import Fruit
# Create your views here.

def index(request):
    return render(request, 'fruits/index.html')

def detail(request, fruit_id):
    response = "{} = {}".format(fruit_id, Fruit.price_of_fruit)
    return HttpResponse(response)
