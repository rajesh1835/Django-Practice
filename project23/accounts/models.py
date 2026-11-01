from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    address = models.TextField()
    profile = models.ImageField()

    username = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username.username
