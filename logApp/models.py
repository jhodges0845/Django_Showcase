from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Log(models.Model):
    comment = models.TextField()
    location = models.CharField(max_length=100)
    event_datetime = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.location