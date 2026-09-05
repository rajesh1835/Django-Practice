from django.db import models

# Create your models here.
class Country(models.Model):
    cid = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=100)

class Capital(models.Model):
    capId = models.IntegerField(primary_key=True)
    capName = models.CharField(max_length=100)
    cid = models.OneToOneField(Country, on_delete=models.CASCADE)