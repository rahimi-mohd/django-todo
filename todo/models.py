from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Todo(models.Model):
    STATUS_CHOICES = {
        1: "In Progress",
        2: "Done",
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    status = models.IntegerField(default=1, choices=STATUS_CHOICES)
    date_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.content