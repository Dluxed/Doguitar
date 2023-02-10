
from django.http import HttpResponse, JsonResponse 
from .models import Project, Tasks
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse("Index page")

def hello(request, username):
    return HttpResponse("<h1>Hello %s<h1>" % username)
    
def about(request):
    return HttpResponse("About")

def project(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe = False)

def tasks(request, title):
    # task = Tasks.objects.get(id=id)
    # task = get_object_or_404(Tasks, id=id)
    task = Tasks.objects.get(title = title)
    return HttpResponse("task: %s" % task.title)

