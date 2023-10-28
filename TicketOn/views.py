from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def Home(request):
    return render(request, 'Home.html')

def index(request):
    return HttpResponse("Welcome to my website")

def signup(request):
    
    return render(request, 'login.html',{
        'form': UserCreationForm
    })

def product_cat(request,product):
    return HttpResponse(f"Here is a list of our {product}.")