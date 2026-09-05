from django.contrib import admin
from .models import Dept, Emp, SalGrade
# Register your models here.
admin.site.register(Dept)
admin.site.register(Emp)
admin.site.register(SalGrade)