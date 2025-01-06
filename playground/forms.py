from django.forms import ModelForm
from . import models

class ProjectForm(ModelForm):
    class Meta:
        model = models.Project
        fields = '__all__' 
        exclude = ['vote_total', 'vote_ratio']

