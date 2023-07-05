from django.urls import path
from . import views

#para ordenar las URLs de myapp
urlpatterns = [

    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('saludar/<str:username>', views.saludar,name="saludar"),
    path('projects/', views.projects, name="projects"),
    path('projects/<int:id>', views.project_detail, name="project_detail"),
    path('tasks/', views.tasks, name="tasks"),
    path('create_task/', views.create_task, name="create_task"),
    path('create_project/', views.create_project, name="create_project"),
    
]