from django.shortcuts import render
import requests
# Create your views here.

# render de chords
def chords(request):    
    response = get_chord({'chordName': 'F_maj7'})
    return render(request, 'chords.html', {
        'chord': response
    })

# CHORDS API requests
def generate_request(url, x={}):    
    response = requests.get(url, params=x)
    if response.status_code == 200:
        return response
    
def get_chord(x={}):
    response = generate_request('https://api.uberchord.com/v1/chords/', x)
    print(x)
    print(response)
    return response