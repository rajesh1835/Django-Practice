from django.shortcuts import render
from .models import Topic, Webpage, AccessRecord
from django.http import HttpResponse

def insert_topic(request):
    tn = input("Enter the Topic Name: ")
    TUTO = Topic.objects.get_or_create(topic_name=tn)
    if TUTO[1]:
        return HttpResponse("New Topic is created 🎉")
    else:
        return HttpResponse("Topic alredy exists! 🙃🌹")

def get_topics(request):
    for to in Topic.objects.all():
        print(to.topic_name)

    return HttpResponse("Available Topics.")

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
    for wpo in Webpage.objects.all():
        print(wpo)
    return HttpResponse("Avalable Webpages")


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
    for aco in AccessRecord.objects.all():
        print(aco)

    return HttpResponse("Retrived Success fully🤩")