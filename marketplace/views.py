from django.http import HttpResponse

def root(request):
    return HttpResponse("This is root route , Next route would be 'playground/home'")