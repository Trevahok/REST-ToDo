from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from datetime import timedelta
import uuid

# Create your models here.
class Task(models.Model):
    title = models.CharField( max_length=50)
    desc = models.CharField( max_length=150)
    completed = models.BooleanField()
    deadline = models.DateTimeField(default=timezone.now() + timedelta(days=1)  , blank=True)
    def __str__(self):
        return self.title
