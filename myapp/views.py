
from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject
# Create your views here.
# primer funcion que retorne un mensaje al cliente o navegador
def index(request):
    #return HttpResponse("Index Page")
    title = 'Proyecto desarrollado con Django y Python con funcion index renderizada'
    return render(request, 'index.html', {
        #diccionario: clave valor
        'title': title
    })


def about(request):
    username = 'futurosProgramadoresArgentina'
    return render(request, 'about.html', {
        'username': username
    })


def saludar(request, username):
    print(username)
    #creamos un parametro que va a ir cambiando
    return HttpResponse("<h1>Hola Mundo desde Mi App %s</h1>" % username)
    # concatenacion "<h2>Hello %s</h2>" % username


def projects(request):
    # projects = list(Project.objects.values())
    # recorre la bd listas de proyectos
    projects = Project.objects.all()
    return render(request, 'projects/projects.html', {
        'projects': projects
    })


def tasks(request):
    # task = Task.objects.get(title=tile)
    # obtener tareas
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.html', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.html', {
            'form': CreateNewTask()
        })
    else:
        Task.objects.create(
            title=request.POST['title'],description=request.POST['description'],project_id=2)
        return redirect('tasks')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.html', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('projects')


def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.html', {
        'project': project,
        'tasks': tasks
    })