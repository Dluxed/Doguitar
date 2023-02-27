from django.shortcuts import render
from .models import Lessons

# Create your views here.
def home(request):
    user = 'Kuro'
    return render(request, '../templates/home.html', {
        'user': user
    })

def login(request):
    return render(request, '../templates/login.html')

def register(request):
    return render(request, '../templates/register.html')

def lessons(request):
    lessons = Lessons.objects.all()
    print(lessons),
    return render(request, '../templates/lecciones.html', {
        'lessons': lessons
    })

def lesson_detail(request, id):
    lesson = Lessons.objects.get(id = id),
    print(lesson),
    return render(request, '../templates/lesson_detail.html', {
        'lesson': lesson 
    })