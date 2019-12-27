from django.db import models

from django.contrib.auth.models import User


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)
    year_start = models.DateField()
    year_end = models.DateField()
    description = models.CharField(max_length=1000)

    def __str__(self):
        return self.role