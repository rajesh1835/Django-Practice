from django.shortcuts import render
from .forms import UserCreateForm, ProfileFoem
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Profile

def create_user(request):
    UFO = UserCreateForm()
    PFO = ProfileFoem()
    context ={"UFO": UFO, "PFO": PFO}

    if request.method == "POST" and request.FILES:
        DUFO = UserCreateForm(request.POST)
        DPFO = ProfileFoem(request.POST, request.FILES)

        if DUFO.is_valid() and DPFO.is_valid():
            MDUFO = DUFO.save(commit=False)

            psw = DUFO.cleaned_data["password"]

            MDUFO.set_password(psw)
            MDUFO.save()

            MDPFO = DPFO.save(commit=False)
            MDPFO.username = MDUFO
            MDPFO.save()

            send_mail("Welcome On boarding ",
                      "You have Successfully registered 🎉",
                      "rajeshtarigonda@gmail.com",
                      [MDUFO.email],
                      fail_silently=False)
            
            return HttpResponse("Created Successfully")
        
        return HttpResponse("Opps..")

    return render(request, "register.html", context)

def bombit(request):
    if request.method == "POST":
        email = request.POST["email"]
        for _ in range(5):
            send_mail("Surprice !!!!",
                    "You got Rs.10000",
                    "rajeshtarigonda@gmail.com",
                    [email],
                    fail_silently=False)
        
    return render(request, "bombit.html")


def home(request):
    if request.session.get("username"):
        username = request.session.get("username")
        d = {"username": username}
        return render(request, "home.html", d)
    
    return render(request, "home.html")


def user_login(request):

    if request.method == "POST":
        un = request.POST["username"]
        psw = request.POST["password"]

        USO = authenticate(username=un, password=psw)

        if USO :
            if USO.is_active:
                login(request, user=USO)
                request.session["username"] = un

                print("logged in successfull")
                return HttpResponseRedirect(reverse("home"))
            return HttpResponse("Not a Active USer")
        return HttpResponse("Invalid Credentials..")

    return render(request, "login.html")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("user-login"))

@login_required
def display_details(request):
    username = request.session.get("username")
    UO = User.objects.get(username=username)
    PO = Profile.objects.get(username=UO)

    context = {"UO":UO, "PO":PO}

    return render(request, "userDetails.html", context)


@login_required
def change_password(request):
    if request.method == "POST":
        username = request.session.get("username")
        password = request.POST["npw"]

        UO = User.objects.get(username=username)
        UO.set_password(password)
        UO.save()
        return HttpResponse("Password Changed Successfully..")
    return render(request, "change_password.html")


def reset_password(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["npw"]
        UO = User.objects.filter(username=username).first()
        if UO:
            UO.set_password(password)
            UO.save()
            return HttpResponseRedirect(reverse("user-login"))
        return HttpResponse("No User Found!")
    return render(request, "reset_password.html")