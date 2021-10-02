from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField()
    description = models.TextField()
    complete = models.BooleanField()
    created = models.DateTimeField()