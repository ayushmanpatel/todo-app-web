from django.db import models
from django.forms import CharField

# Create your models here.

class Todo(models.Model):
    todo = models.CharField(max_length=1000)

    def __str__(self):
        return self.todo
