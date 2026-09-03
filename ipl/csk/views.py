from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def captain(request):
    return HttpResponse("<h1>MS DHONI 😎</h1>")

def viceCaptain(request):
    return HttpResponse("<h2>Ruthraj Gaikwad 🤩</h2>")
