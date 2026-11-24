from django.db import models
from django.urls import reverse

class School(models.Model):
    scname = models.CharField(max_length=100)
    scloc = models.CharField(max_length=100)
    scprincepal = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.scname

    def get_absolute_url(self):
        return reverse('SchoolDetails',kwargs={'pk':self.pk})

class Students(models.Model):
    scname = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name