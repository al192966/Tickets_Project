from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def Home(request):
    return render(request, 'Home.html')

def signup(request):
    
    return render(request, 'login.html',{
        'form': UserCreationForm
    })