from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse 
from .models import Project, Tasks 
import datetime




# Create your views here.
def index(request):
    return HttpResponse("<h1>Wenas nocheeees</h1>")

def hello(request, username):
    return HttpResponse("<h1>Hello %s<h1>" % username)
    
def about(request):
    return HttpResponse("About")

def project(request):
    projects = Project.objects.all()
    #projects = list(Project.objects.values())
    #return JsonResponse(projects, safe = False)
    return render(request, '../templates/testMess.html', {
        'projects': projects
    })

def tasks(request, title):
    # task = Tasks.objects.get(id=id)
    task = get_object_or_404(Tasks, title=title)
    #task = Tasks.objects.get(title = title)
    return HttpResponse("task: %s" % task.title)

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>"
    return HttpResponse(html)