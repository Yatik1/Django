from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    # return HttpResponse("Hello World")
    return render(request, 'hello.html', {'name':'Yatik'})

def say_bye(request):
    return HttpResponse("Good bye Friend!!")

def dyn_params(request,pk): 
    return HttpResponse('Dynamic Param :' + str(pk))