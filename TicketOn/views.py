from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponse

# Create your views here.


def Home(request):
    return render(request, 'Home.html')


def index(request):
    return HttpResponse("Welcome to my website")


def signup(request):

    if request.method == 'GET':
        return render(request, 'login.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registro de usuario
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('eventos')
            except IntegrityError:
                return render(request, 'login.html', {
                    'form': UserCreationForm,
                    "error": 'Usuario ya existe'
                })

        return render(request, 'login.html', {
            'form': UserCreationForm,
            "error": 'Contraseñas no coinciden'
        })

def eventos(request):
    return render (request,'Eventos.html')

def CS(request):
    logout(request)
    return redirect('home')

def IS(request):
    return render (request, 'signin.html')