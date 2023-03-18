from django.urls import path
from . import views

urlpatterns = [
    path('', views.chords, name='chords'),
    path('<str:chord>', views.chords, name='chords')
]