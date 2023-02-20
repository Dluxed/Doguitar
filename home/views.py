from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, '../templates/home.html')

def login(request):
    return render(request, '../templates/login.html')

def register(request):
    return render(request, '../templates/register.html')

def lessons(request):
    return render(request, '../templates/lecciones.html')