from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Lessons
# Create your views here.
def chord_library(request):
    return render(request, '../templates/chords.html')

def lesson_detail(request, id):
    #CUIDADO CON LAS COMAS AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    p = get_object_or_404(Lessons, id=id)
    #print([x.title for x in p]),
    return render(request, '../templates/lesson_detail.html', {
        'p': p,
        'image': p.image 
        #'lesson': lesson
    })

def lessons(request):
    lecciones = Lessons.objects.all()
    #print(lessons)
    return render(request, '../templates/lecciones.html', {
        'lecciones': lecciones
    })

def get_image(request, id):
    obj = Lessons.objects.get(id=id)
    image_data = obj.image.read()
    response = HttpResponse(image_data, content_type='image/jpeg')
    return response