from django.db import models

class Event(models.Model):
    Song = models.CharField(max_length = 30)
    Artist = models.CharField(max_length = 30)
    Genre = models.CharField(max_length = 30)