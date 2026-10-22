from django.shortcuts import render
from .forms import UserForm, WebPageModelForm
from django.http import HttpResponse

def user_create(request):
    EUFO = UserForm()
    context = {"EUFO":EUFO}

    if request.method == "POST":
        DUO = UserForm(request.POST)
        if DUO.is_valid():
            print(DUO.cleaned_data)
            return HttpResponse(str(DUO.cleaned_data))
        else:
            return HttpResponse("Invalid Data")
    return render(request, "user.html", context)

def create_webpages(request):
    EWFO = WebPageModelForm()
    context = {"EWFO": EWFO}

    if request.method == "POST":
        WFDO = WebPageModelForm(request.POST)

        if WFDO.is_valid():
            WFDO.save()
            return HttpResponse("Created...,.")
        return HttpResponse("Invalid Data")
    
    return render(request, "createWebpage.html", context)