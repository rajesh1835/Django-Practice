from django.shortcuts import render
from .models import Dept, Emp, SalGrade
from django.http import HttpResponse

def insert_employee(request):
    print("*** Available Departments ***")
    for do in Dept.objects.all():
        print(do.deptno, do.dname)

    dno = int(input("Enter Dept No: "))
    LDO  = Dept.objects.filter(deptno=dno)
    if LDO:
        deptno = LDO[0]
        empno = int(input("Enter the Employee No: "))
        ename = input("Enter Empoyee Name: ")
        job = input("Enter Employee Job: ")
        sal = int(input("Enter Employee Salary: "))
        comm = input("Enter the Commission: ")
        if comm:
            comm = int(comm)
        else:
            comm = None

        for mo in Emp.objects.all():
            print(mo.empno)
        
        mgr = input("Enter the MGR No: ")
        if mgr:
            mgr = Emp.objects.filter(empno=mgr)[0]
        else:
            mgr=None

        TEO = Emp.objects.get_or_create(empno=empno, ename=ename, job=job, sal=sal, comm=comm, deptno=deptno, mgr=mgr)
        if TEO[1]:
            return HttpResponse("Employee Created Successfully..")
        else:
            return HttpResponse("Employee Already Exists..")
     
    return HttpResponse("Dept No not exists!")

def display_departments(request):
    QSDO = Dept.objects.all()   
    context = {"QSDO": QSDO}

    return render(request, "display_dept.html", context)

def display_employees(request):
    QSEO = Emp.objects.all()
    QSEO = Emp.objects.filter(ename__startswith="s")
    QSEO = Emp.objects.filter(ename__endswith="s")
    QSEO = Emp.objects.filter(ename__contains="e")

    QSEO = Emp.objects.filter(deptno__in=(20,30))
    QSEO = Emp.objects.filter(hiredate__year="2026")


    context = {"QSEO" : QSEO}

    return render(request, "display_emp.html", context)
    