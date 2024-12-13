from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#
#
# Views function take request and send response, thus called request handler
# In some other languages called "actions" , and in django called "Views"

def say_hello(request):
    return HttpResponse("Hello World")

def hello(request):
    return render(request,'hello.html', {'name':'Mosh'} ) 