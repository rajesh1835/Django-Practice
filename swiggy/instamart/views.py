from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "instamart.html")

def ice_cream(request):
    return HttpResponse("<h1>Buttter Scotch </h1>")

def biscuits(request):
    return HttpResponse("<h1>Parle-G, Bourbon, Happy Happy</h1>")

