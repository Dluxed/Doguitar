from django.shortcuts import render
import requests, json
from lessons import models
# Create your views here.

# render de chords
def chords(request, chord):    
    response = get_chord(chordName = chord)
    l = models.Lessons.objects.all()
    return render(request, 'chords.html', {
        'chord': response,
        'lecciones': l
    })

# CHORDS API requests
def get_chord(chordName):
    response = generate_request('https://api.uberchord.com/v1/chords/' + chordName)
    return response

# Requests
def generate_request(url): 
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
      
    
    