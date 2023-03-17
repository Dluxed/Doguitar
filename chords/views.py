from django.shortcuts import render
import requests, json
# Create your views here.

# render de chords
def chords(request):    
    response = get_chord('F_maj7')
    return render(request, 'chords.html', {
        'chord': response
    })

# CHORDS API requests

def get_chord(chordName):
    response = generate_request('https://api.uberchord.com/v1/chords/' + chordName)
    return response

def generate_request(url): 
   
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
      
    
    