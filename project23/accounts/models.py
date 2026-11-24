from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    address = models.TextField()
    profile = models.ImageField()

    username = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.username.username


class WeatherData(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    temperatue = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)
    weather = models.DecimalField(max_digits=5, decimal_places=2)
    speed = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.city 
