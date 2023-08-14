from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from . models import Project, Task

def index( request ):
    title = "Django Project!!"
    return render(request, 'index.html',{
        'title': title
    })
      

def hello( request, username ):
    print(username)
    return HttpResponse('Hello %s' % username)

def about( request ):
    return HttpResponse('<h1>about us</h1>')

def products( request ):
    return HttpResponse('<h1>products</h1>')

def operation( request, number ):
    result = (number + 100) * 2
    return HttpResponse('<h2>el resultado es (%s + 100) * 2 es %s </h2>' % (number, result))

# Listando todos los proyectos
def projects( request ):
    title = "projects"
    projects = list(Project.objects.values())
    return render(request, 'projects.html', {
        'title': title,
        'projects': projects 
    })


#Listar una tarea
def tasks(request, id):
    #task = get_object_or_404(Task, id=id)
    #return render(request, 'tasks.html', {
     #   'title': title ,
    #    'tasks' : tasks
    #})
    tasks =  Task.objects.all()
    return render( request, 'tasks.html' , {
        'tasks' : tasks
    })








