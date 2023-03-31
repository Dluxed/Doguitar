from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Lessons
# Create your views here.
def chord_library(request):
    return render(request, '../templates/chords.html')

def lesson_detail(request, id):
    #CUIDADO CON LAS COMAS AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
    obj = get_object_or_404(Lessons, id=id)
    allL = Lessons.objects.all()
    #print([x.title for x in p]),
    print(obj.description) 
    return render(request, 'lesson_detail.html', {
        'lesson': obj,
        'description': obj.description,
        'image': obj.image,
        'lecciones': allL
        
        #'lesson': lesson
    })

def lessons(request):
    l = Lessons.objects.all()
    #print(lessons)
    return render(request, '../templates/lecciones.html', {
        'lecciones': l
    })

def get_image(request, id):
    obj = Lessons.objects.get(id=id)
    image_data = obj.image.read()
    response = HttpResponse(image_data, content_type='image/jpeg')
    return response

def setDone(request, id):
    less = Lessons.objects.get(id=id)
    less.finished = True
    less.save()

    obj = get_object_or_404(Lessons, id=id)
    allL = Lessons.objects.all()
    
    return render(request, 'lesson_detail.html', {
        'lesson': obj,
        'description': obj.description,
        'image': obj.image,
        'lecciones': allL
        
        #'lesson': lesson
    })
