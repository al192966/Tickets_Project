from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.

def Home(request):
    return render(request, 'Home.html')

def index(request):
    return HttpResponse("Welcome to my website")

def signup(request):
    

    if request.method =='GET':
        return render(request, 'login.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            #registro de usuario
            try:
                user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                user.save()
                return HttpResponse('Usario Creado Correctamente')
            except:
                return HttpResponse('Usuario ya existe')
        return HttpResponse ('Las contraseñas no coinciden'),
