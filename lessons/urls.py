from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.lessons, name='lessons'),

    # Renderiza la pagina
    path('<int:id>', views.lesson_detail, name="lesson_detail"),

    # Solicita imagen del servidor
    path('image/<int:id>', views.get_image, name='get_image'),

    path('setDone/<int:id>', views.setDone, name='setDone'),

]