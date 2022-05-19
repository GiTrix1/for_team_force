from django.contrib.auth.models import User
from django.db import models


class Skills(models.Model):
    skill = models.CharField(max_length=500)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=500)
    middle_name = models.CharField(max_length=500)
    last_name = models.CharField(max_length=500)
    skills = models.CharField(null=True, max_length=500)
    language = models.CharField(max_length=500)
    hobbies = models.CharField(max_length=500)
