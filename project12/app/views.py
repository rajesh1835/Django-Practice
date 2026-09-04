from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")

def rcb(request):
    return render(request, "rcb.html")
