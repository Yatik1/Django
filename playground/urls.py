from django.urls import path
from . import views

# URL configuration
urlpatterns = [
    path("hello/" , views.say_hello),
    path("content/", views.hello, name="hello"),
]   