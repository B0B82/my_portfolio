from django.db import models
from datetime import datetime


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(blank=True, upload_to='my_portfolio/img')
    date = models.DateTimeField(default=datetime.now)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title