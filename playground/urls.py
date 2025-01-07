from django.urls import path
from . import views

urlpatterns = [
    path("hello/" , views.say_hello,name="hello"),
    path("bye/", views.say_bye,name="bye"),
    path("params/<str:pk>/", views.dyn_params),  ## this is for dynamic routing 
    path("getall/",views.get_all_projects,name="getall"),
    path("getproject/<str:id>/",views.get_project),
    path("create/",views.create_project,name='create_project')
]