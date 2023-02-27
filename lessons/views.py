from django.shortcuts import render

# Create your views here.
def chord_library(request):
    return render(request, '../templates/chords.html')