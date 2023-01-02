from django.db import models
from datetime import date


# Create your models here.
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    pwd = models.CharField(max_length=32)


class CV(models.Model):
    name = models.CharField(max_length=32)
    date = models.DateField(default=date.today)
    content = models.TextField()
    if_follow = models.BooleanField(default=False)
