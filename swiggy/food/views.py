from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "food.html")

def biryani(request):
    return HttpResponse("Chicken Biryani .....")

def dosa(request):
    return HttpResponse("Masala Dosa, with chutny......😊")