from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from . import models

# Create your views here.
def say_hello(request):
    # return HttpResponse("Hello World")
    return render(request, 'hello.html', {'name':'Yatik'})

def say_bye(request):
    return HttpResponse("Good bye Friend!!")

def dyn_params(request,pk): 
    return HttpResponse('Dynamic Param :' + str(pk))

def get_all_projects(request):
    projects = models.Project.objects.all()
    json_projects = serializers.serialize('json',projects)
    return HttpResponse(json_projects, content_type='application/json')

def get_project(request,id):
    project = models.Project.objects.get(pk=id)
    print(project)

    tag = project.tag.all()
    print(tag)

    json_project = serializers.serialize('json',[project])
    return HttpResponse(json_project,content_type='application/json')