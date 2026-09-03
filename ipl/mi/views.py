from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def captain(request):
    return HttpResponse("<h1>ROHIT SHARMA (HITMAN) 🤩</h1>")

def viceCaptain(request):
    return HttpResponse("<h2>HARDIK PANDYA ☠️</h2>")
