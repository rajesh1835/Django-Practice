from django import forms
from .models import Emp


class EmployeeCreateForm(forms.ModelForm):
    class Meta:
        model = Emp
        fields = "__all__"

        widgets = {"deptno": forms.RadioSelect}