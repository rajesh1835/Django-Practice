from django.shortcuts import render
from .models import Dept, Emp, SalGrade
from django.http import HttpResponse
from django.db.models import Q, Avg, F, Prefetch

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
    QSEO = Emp.objects.filter().values('ename')
    QSEO = Emp.objects.filter().values('ename','deptno')
    QSEO = Emp.objects.filter().values('ename','comm')
    QSEO = Emp.objects.filter(ename="BLAKE")
    QSEO = Emp.objects.filter(sal__gt=2000)
    QSEO = Emp.objects.filter(job="SALESMAN")
    QSEO = Emp.objects.filter(hiredate__year__gt=1982)
    QSEO = Emp.objects.filter(job="CLERK").values("sal")
    QSEO = Emp.objects.filter(ename="JONES")
    QSEO = Emp.objects.filter(hiredate__gt='1981-01-01')
    QSEO = Emp.objects.filter(sal__gt=2000, sal__lte=3500)

    QSEO = Emp.objects.filter(job__in=("MANAGER", "CLERK"))
    QSEO = Emp.objects.filter(Q(job__in=("MANAGER", "CLERK")) | Q(deptno=10))
    QSEO = Emp.objects.exclude(job="SALESMAN")
    QSEO = Emp.objects.filter(job="SALESMAN", deptno__in=(10,30))
    QSEO = Emp.objects.filter(job__in=("MANAGER", "CLERK"), deptno__in=(10,30))
    QSEO = Emp.objects.filter(empno__in=(7902, 7839))
    QSEO = Emp.objects.filter(hiredate__year__gt="1981", deptno__in=(10,30))
    QSEO = Emp.objects.filter(sal__range=(1000, 4000))
    QSEO = Emp.objects.exclude(job__in=("ANALYST", "MANAGER"))
    QSEO = Emp.objects.filter(hiredate__range=("1981-01-01", "1987-12-31"))
    QSEO = Emp.objects.filter(comm=None)
    


    context = {"QSEO" : QSEO}

    return render(request, "display_emp.html", context)


def empToDept(request):
    QSLEDO = Emp.objects.all().select_related("deptno")
    QSLEDO = Emp.objects.select_related("deptno").all()
    QSLEDO = Emp.objects.filter(sal__gt=2000).select_related("deptno")
    QSLEDO = Emp.objects.filter(sal__lt=2000, deptno=20).select_related("deptno")
    QSLEDO = Emp.objects.filter(deptno__dname="ACCOUNTING").select_related("deptno")
    QSLEDO = Emp.objects.filter(deptno__dname__contains="a").select_related("deptno")
    QSLEDO = Emp.objects.filter(mgr=7839).select_related("deptno")
    QSLEDO = Emp.objects.filter(hiredate__year__gt=1983).select_related("deptno")
    QSLEDO = Emp.objects.filter(empno__in=(7839,7902), deptno__loc="NEW YORK").select_related("deptno")


    context = {"QSLEDO" : QSLEDO}

    return render(request, "empToDept.html", context)


def empToMgr(request):
    QSEMO = Emp.objects.all().select_related("mgr")
    QSEMO = Emp.objects.filter(sal__gt=2000, mgr__sal__lt=5000, deptno=F("mgr__deptno")).select_related("mgr", "deptno")
    QSEMO = Emp.objects.filter(mgr__deptno__in=(10,20)).select_related("mgr")
    QSEMO = Emp.objects.filter(job="SALESMAN", mgr__deptno=30).select_related("mgr")
    QSEMO = Emp.objects.filter(hiredate__lte=F("mgr__hiredate")).select_related("mgr")
    QSEMO = Emp.objects.filter(mgr__sal__endswith="50").select_related("mgr")

    context = {"QSEMO" : QSEMO}

    return render(request, "empToMgr.html", context)


def empToMgrADept(request):
    QSEMDO = Emp.objects.all().select_related("mgr", "deptno")
    QSEMDO = Emp.objects.filter(mgr__deptno__loc='NEW YORK', mgr__sal__gt=3000).select_related("mgr", "deptno")

    context = {"QSEMDO" : QSEMDO}

    return render(request, "empToMgrADept.html", context)


def deptToEmpPR(request):
    QSDEO = Dept.objects.prefetch_related("emp_set")
    QSDEO = Dept.objects.prefetch_related("emp_set").filter(dname="RESEARCH")
    QSDEO = Dept.objects.prefetch_related("emp_set").filter(loc="CHICAGO")

    QSDEO = Dept.objects.prefetch_related(Prefetch("emp_set", queryset=Emp.objects.filter(sal__gt=2000)))



    context = {"QSDEO" : QSDEO}

    return render(request, "deptToEmpPR.html",context)


def updateEmployees(request):
    Emp.objects.filter(ename="Robin").update(sal=F('sal')+100)

    QSEO = Emp.objects.all()

    context = {"QSEO" : QSEO}

    return render(request, "display_emp.html", context)


def create_employee(request):
    QLDO = Dept.objects.all()
    QLMO = Emp.objects.all()
    context = {"QLDO": QLDO, "QLMO": QLMO}

    if request.method == "POST":
        empno = request.POST["empno"]
        ename = request.POST["ename"]
        job = request.POST["job"]
        sal = request.POST["sal"]
        comm = request.POST["comm"]
        mgr = request.POST["mgr"]
        deptno = request.POST["deptno"]

        MO = Emp.objects.get(empno= mgr)
        DO = Dept.objects.get(deptno= deptno)

        TEO = Emp.objects.get_or_create(empno=empno, ename=ename, job=job, sal=sal, comm=comm, mgr=MO, deptno=DO)

        if TEO[1]:
            print("Created Successfully..")
        else:
            print("Already Exixts!")
        return render(request, "createEmployee.html", context)

    return render(request, "createEmployee.html", context)