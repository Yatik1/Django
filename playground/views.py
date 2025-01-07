from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.core import serializers
from . import models
from . import forms

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

def create_project(request):
    form = forms.ProjectForm()

    # if request.method == 'POST':
        # form_data = request.POST
        # print("Form data:" , form_data)
        # title = form_data['title']
        # print("Project Title" , title)

    if request.method == 'POST':
        form = forms.ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('getall') # getall is url name, check urls file for name
            # return HttpResponse("Project Created Successfully")

    context = {'form':form}
    return render(request,'form.html',context)