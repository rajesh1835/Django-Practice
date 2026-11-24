import csv

from django.shortcuts import render
from .models import Bank, Branch, BusinessEmployemntData
from django.http import HttpResponse

def insert_bank(request):
    file = "D:\\projects\\Django\\project24\\app1\\bank.csv"

    with open(file, "r") as FO:
        IDO = csv.reader(FO)
        for bank in IDO:
            bname = bank[0].strip()

            Bank.objects.get_or_create(bank_name=bname)
    return HttpResponse("Banks created Successfully..")

def insert_branches(request):
    file = "D:\\projects\\Django\\project24\\app1\\branches.csv"

    with open(file, "r") as FO:
        IBO = csv.reader(FO)
        next(IBO)

        for data in IBO:
            bname = data[0].strip()

            LBO = Bank.objects.filter(bank_name=bname)

            if LBO:
                ifsc = data[1]
                branch = data[2]
                address = data[3]
                mobile = data[4]
                city = data[5]
                district = data[6]
                state = data[7]

                Branch.objects.get_or_create(bank_name=LBO[0], ifsc=ifsc, branch=branch, address=address, mobile=mobile, city=city, district=district, state=state)

        return HttpResponse("all branches created successfully..")
            

    
def insert_business(request):
    file = "D:\\projects\\Django\\project24\\app1\\Business-employment-data.csv"

    with open(file, "r") as FO:
        IBSO = csv.reader(FO)
        next(IBSO)   

        for data in IBSO:
            bo = BusinessEmployemntData(series_reference=data[0], period=data[1], data_value=data[2], suppressed=data[3], status=data[4],units=data[5], magnitude=data[6], subject=data[7], group=data[8], series_title1=data[9], series_title2=data[10])
            bo.save()

        return HttpResponse("Business Data inserted sccessfully..")
