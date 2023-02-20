from django.urls import path
from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    path('', views.index),
    #path('admin/', )
    path('about/', views.about),
    path('hello/<str:username>', views.hello),
    path('projects/', views.project),
    path('tasks/<str:title>', views.tasks),
    path('datetime', views.current_datetime)
]

