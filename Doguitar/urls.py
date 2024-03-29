"""Doguitar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import urls
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [    
    #urls(r'^login/', include('login.urls')),
    path('', views.home, name="home"),
    path('admin/', admin.site.urls),

    # urls
    path('chords/', include('chords.urls'), name='chords'),
    path('lessons/', include('lessons.urls')),
    path('tuner/', views.tuner, name='tuner'),
    path('profile/', views.profile, name='profile'),
   

    # Authenitication urls
    path('login/', views.signin, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.signout, name='logout'),
    
    #All auth authentication urls
    path('accounts/', include('allauth.urls')),
    #path('testRegister/', views.testRegister, name='testRegister')
]
