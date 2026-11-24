"""
URL configuration for project27 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app1.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("stringCbv/", stringCbv.as_view(), name="stringCbv"),
    # path("InsertByTV/", InsertByTV.as_view(), name="InsertByTV"),
    # path("InsertByFV/", InsertByFV.as_view(), name="InsertByFV"),
    path("SchoolList/", SchoolList.as_view(), name="SchoolList"),
    path("SchoolCreate/", SchoolCreate.as_view(), name="SchoolCreate"),

    re_path("^update/(?P<pk>\d+)/", SchoolUpdate.as_view(), name= "SchoolUpdate"),
    re_path("^delete/(?P<pk>\d+)/", SchoolDelete.as_view(), name= "SchoolDelete"),


    re_path("(?P<pk>\d+)/", SchoolDetails.as_view(), name="SchoolDetails"),


]
