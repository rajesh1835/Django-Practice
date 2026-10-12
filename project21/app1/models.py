from django.db import models
from django import forms
# Create your models here.
class Topic(models.Model):
    topic_name = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.topic_name

def checkmobile(number):
    if len(number) != 10:
        raise forms.ValidationError("Mobile number will contain 10.")
    
class Webpage(models.Model):
    topic_name = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField()
    url = models.URLField()
    email = models.EmailField(null=True, blank=True)
    mobile = models.CharField(max_length=10, validators=[checkmobile])

    def __str__(self):
        return self.name
