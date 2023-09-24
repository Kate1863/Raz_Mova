from django.shortcuts import render
from django.http import HttpResponse
from random import randint

# Create your views here.

def get_random(request):
    return HttpResponse("<h1>Result:</h1>" + str(randint(0, 500)))
