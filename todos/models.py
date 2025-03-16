from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title