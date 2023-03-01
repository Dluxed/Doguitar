from django.shortcuts import render, get_object_or_404
from .models import Lessons
# Create your views here.
def chord_library(request):
    return render(request, '../templates/chords.html')

def lesson_detail(request, id):
    #CUIDADO CON LAS COMAS AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    p = get_object_or_404(Lessons, id=id)
    #print([x.title for x in p]),
    return render(request, '../templates/lesson_detail.html', {
        'p': p 
        #'lesson': lesson
    })

def lessons(request):
    lecciones = Lessons.objects.all()
    #print(lessons)
    return render(request, '../templates/lecciones.html', {
        'lecciones': lecciones
    })