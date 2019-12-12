from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=100)
    organised_on = models.DateTimeField('date published')
    organising_head = models.CharField(max_length=100)
    organising_budget = models.IntegerField(default=0)
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.name