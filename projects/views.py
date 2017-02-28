from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index():
    HttpResponse("This the the D3 project")

def d3():
    return HttpResponse("This is the d3 project")
