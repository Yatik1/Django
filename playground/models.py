from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    id=models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    title=models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
    demo_link=models.CharField(max_length=2000,blank=True,null=True)
    source_link=models.CharField(max_length=2000,blank=True,null=True)
    tag=models.ManyToManyField('Tag',blank=True)
    vote_total = models.IntegerField(default=0)
    vote_ratio = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class Review(models.Model):

    VOTE_TYPE = (
        ('up','up'),
        ('down','down')
    )

    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4 , primary_key=True, editable=False, unique=True)

    def __str__(self):
        return self.value
    
class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

