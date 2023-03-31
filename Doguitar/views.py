from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from lessons import models

# HOME render
def home(request):
    l = models.Lessons.objects.all()
    return render(request, '../templates/home.html', { 'lecciones': l })

# SIGNIN render
def signin(request):
    # Si es una solicitud renderiza
    if request.method == 'GET':
        return render(request, '../templates/login.html')
    
    #Si es un formulario envia
    else:   
        #Autentica el usuario
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        #Si no esta autenticado imprime 
        if user is None: 
            return render(request, '../templates/login.html', {
                'error': "Usuer or password is incorrect"
            })
        #Si ya esta autenticado redirije
        else:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')

def signout(request):
    logout(request)
    return redirect('home')

def register(request):
    # Si es solicitud renderiza
    if request.method == 'GET':
        #print("enviando formulario")
        return render(request, '../templates/register.html', {
            'form': UserCreationForm
        })
    # Envia el formulario
    else:
        #print(request.POST)
        #print("obteniendo datos")

        #Verifica contraseñas
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                #return HttpResponse("User created successfully")
                return redirect('home')
            except IntegrityError:
                #return HttpResponse("User already exists!")
                return render(request, '../templates/register.html', {
                    'form': UserCreationForm,
                    'error': "Username already exists!"
                })
        else:
            #return HttpResponse("Passwords do not match!!")
            return render(request, '../templates/register.html', {
                'form': UserCreationForm,
                'error': "passwords do not match"
            })


def tuner(request):    
    return render(request, 'tuner.html')

def profile(request):    
    return render(request, 'profile.html')


