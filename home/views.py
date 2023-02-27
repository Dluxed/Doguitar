from django.shortcuts import render, get_object_or_404, redirect
from .models import Lessons
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from django.db import IntegrityError
# Create your views here.
def home(request):
    return render(request, '../templates/home.html')

def signin(request):
    if request.method == 'GET':
        return render(request, '../templates/login.html', {
            'form': AuthenticationForm
        })
    else: 
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, '../templates/login.html', {
                'form': AuthenticationForm,
                'error': "Usuer or password is incorrect"
            })
        else:
            login(request, user)
            return redirect('home')

def signout(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'GET':
        #print("enviando formulario")
        return render(request, '../templates/register.html', {
            'form': UserCreationForm
        })
    else:
        #print(request.POST)
        #print("obteniendo datos")
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
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


    

def lessons(request):
    lessons = Lessons.objects.all()
    print(lessons)
    return render(request, '../templates/lecciones.html', {
        'lessons': lessons
    })

#Nota: 
    #El ciclo de python luce asi pero exporta con simbolos adicionales en los valores
    #El ciclo de jinja ya ignora los valores adicionales.... so its better
        #lesson = [x.title for x in p], 
    
def lesson_detail(request, id):
    #CUIDADO CON LAS COMAS AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    p = get_object_or_404(Lessons, id=id)
    
    #print([x.title for x in p]),
    
    return render(request, '../templates/lesson_detail.html', {
        'p': p 
        #'lesson': lesson
    })

def chords(request):    
    return render(request, 'chords.html')