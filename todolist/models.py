from django.db import models
from season.models import User

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    datecreated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)
    datecompleted = models.DateTimeField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
