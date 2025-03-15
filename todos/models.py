from django.db import models
from django.urls import reverse

# Create your models here.

class TodoModel(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    slug = models.SlugField(default="",null=False)
    
    def __str__(self):
        return self.title
    