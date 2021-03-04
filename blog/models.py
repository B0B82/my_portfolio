from django.db import models
from time import time
from datetime import datetime


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
