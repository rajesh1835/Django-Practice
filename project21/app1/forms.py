from django import forms
from .models import Webpage

class UserForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    url = forms.URLField()
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput)
    gender = forms.ChoiceField(choices=[("male", "male"), ("female", "female")], widget=forms.RadioSelect)


class WebPageModelForm(forms.ModelForm):
    class Meta:
        model = Webpage
        fields = "__all__"
    reenteremail = forms.EmailField()

    def clean(self):
        email = self.cleaned_data["email"]
        reenteremail = self.cleaned_data["reenteremail"]

        if email != reenteremail:
            raise forms.ValidationError("email doesnot match")