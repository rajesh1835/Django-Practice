from django.shortcuts import render
from .models import Topic, Webpage, AccessRecord
from django.http import HttpResponse
from django.db.models.functions import Length

def insert_topic(request):
    if request.method == "POST":

        tn = request.POST["tname"]
        TUTO = Topic.objects.get_or_create(topic_name=tn)
        if TUTO[1]:
            return HttpResponse("New Topic is created 🎉")
        else:
            return HttpResponse("Topic alredy exists! 🙃🌹")

    return render(request, "createTopics.html")

def get_topics(request):
    QSTO = Topic.objects.all()
    context = {"QSTO": QSTO}
    
    return render(request, "display_topics.html", context)

def insert_webpage(request):
    print("--- Available Topics ---")
    for to in Topic.objects.all():
        print(to)

    tn = input("Enter the topic name: ")
    LTO = Topic.objects.filter(topic_name=tn)

    if LTO:
        name = input("Enter the Webpage name: ")
        url = input("Enter the Webpage url: ")
        email = input("Enter the Webpage email: ")
        mobile = input("Enter the Webpage mobile: ")

        TUWO = Webpage.objects.get_or_create(topic_name=LTO[0], name=name, url=url, email=email, mobile=mobile)

        if TUWO[1]:
            return HttpResponse("Web Page is created Successfully 🎉🎉🎉")
        else:
            return HttpResponse("Already Exists🙃")
    else:
        return HttpResponse("Web page is not Created!!🤡")



def get_webpages(request):
    QSWO = Webpage.objects.all()
    QSWO = Webpage.objects.order_by("topic_name")
    QSWO = Webpage.objects.order_by(Length("name").desc())

    context = {"QSWO": QSWO}

    return render(request, "display_webpages.html", context)


def insert_access_records(request):
    names = Webpage.objects.all()
    print("--- Avaialable Names ---")
    for name in names:
        print(name)

    name = input("Eneter the Name: ")
    LWO = Webpage.objects.filter(name = name)

    if LWO:
        author = input("Enter Author Name: ")
        ACO = AccessRecord.objects.get_or_create(name= LWO[0], author=author)
        if ACO[1]:
            return HttpResponse("Access Record Cerated Successfully.🎉🎉")
        else:
            return HttpResponse("Something Went Wrong ☠️")
    else:
        return HttpResponse("Name does not exist!")


def get_access_records(request):
    QSARO = AccessRecord.objects.all()

    context = {"QSARO": QSARO}

    return render(request, "display_access_records.html", context)



def update_webpages(request):

    # Webpage.objects.filter(topic_name="CRICKET").update(email="vk@gmail.com")

    # Webpage.objects.filter(name="robin").update(email="robin@gmail.com")

    # Webpage.objects.filter(topic_name="BGMI").update(url="https://bgmi.in")



    QSWO = Webpage.objects.all()
    context = {"QSWO": QSWO}
    
    return render(request, "display_webpages.html", context)



def create_webpages(request):
    TO = Topic.objects.all()
    context = {"TO": TO}

    if request.method == "POST":
        tname = request.POST["tn"]
        name = request.POST["name"]
        url = request.POST["url"]
        email = request.POST["email"]
        mobile = request.POST["number"]

        LTO = Topic.objects.get(topic_name=tname)

        TWO = Webpage.objects.get_or_create(topic_name=LTO, name=name, url=url, email=email, mobile=mobile)

        if TWO[1]:
            print("Web page created successfully..")
        else:
            print("Oooppppsssssssssssss!!!!!!!")
        
        return render(request, "createWebpage.html", context)
        
    
    
    return render(request, "createWebpage.html", context)


def create_access_records(request):
    WPO = Webpage.objects.all()
    context = {"WPO": WPO}

    if request.method == "POST":
        wid = request.POST["pk"]
        author = request.POST["author"]

        NO = Webpage.objects.get(id=wid)

        ARO = AccessRecord.objects.get_or_create(name=NO, author=author)

        if ARO[1]:
            print("Created....")
        else:
            print("Opps.....")

        return render(request, "createAccessRecord.html", context)
    
    return render(request, "createAccessRecord.html", context)


def select_multiple_topics(request):
    if request.method == "POST":
        QSWO = Webpage.objects.none()
        topics = request.POST.getlist("topics")

        for topic in topics:
            QSWO = QSWO | Webpage.objects.filter(topic_name=topic)
        d = {"QSWO": QSWO}

        return render(request, "display_webpages.html", d)
    QLTO = Topic.objects.all()
    print(QLTO)
    context = {"QLTO": QLTO}
    return render(request, "selectMultipleTopics.html", context)


def select_multiple_web_pages(request):
    if request.method == "POST":
        QSARO = AccessRecord.objects.none()

        webpages = request.POST.getlist("webpages")

        for wid in webpages:
            QSARO = QSARO | AccessRecord.objects.filter(id = wid)

        d = {"QSARO": QSARO}
        return render(request, "display_access_records.html", d)
    
    QLWO = Webpage.objects.all()
    context = {"QLWO" : QLWO}
    return render(request, "selectMultipleWebPages.html", context)


def checkbox_topics(request):
    QLTO = Topic.objects.all()
    context = {"QLTO" : QLTO}
    return render(request, "checkbox_topics.html", context)

def checkbox_webpages(request):
    QLWO = Webpage.objects.all()
    context = {"QLWO": QLWO}

    return render(request, "checkbox_webpages.html", context)