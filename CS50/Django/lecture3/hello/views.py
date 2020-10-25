from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def frank(request):
    return HttpResponse("Hello, Frank!")

def charlotte(request):
    return HttpResponse("Hello, Charlotte!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })