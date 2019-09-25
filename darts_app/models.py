import datetime

from django.db import models
from django.utils import timezone


class User(models.Model):
    user_name = models.CharField(max_length=20, default=0)
    register_date = models.DateTimeField("date registered")

    def __str__(self):
        return self.user_name

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    score = models.PositiveIntegerField(default=0)
    register_date = models.DateTimeField("date registered")

    def __str__(self):
        return self.user_id
    