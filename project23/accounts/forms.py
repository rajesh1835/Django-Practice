from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        help_texts = {"username": ""}
        fields = ["email", "username", "password"]
        widgets = {"password": forms.PasswordInput()}


class ProfileFoem(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ["username"]
