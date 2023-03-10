from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.lessons, name='lessons'),
    path('<int:id>', views.lesson_detail, name="lesson_detail"),
    path('image/<int:id>', views.get_image, name='get_image')
]