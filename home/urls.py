from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('lessons/', views.lessons, name="lessons"),
    path('lessons/<int:id>', views.lesson_detail, name="lesson_detail")
]