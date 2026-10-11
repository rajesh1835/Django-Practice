from django import forms
from .models import Topic, Webpage

class WebPageCreateForm(forms.Form):
    topic_name = forms.ModelChoiceField(queryset=Topic.objects.all())
    name = forms.CharField()
    url = forms.URLField()
    email = forms.EmailField()
    mobile = forms.CharField()


class AccessRecordCreateForm(forms.Form):
    name = forms.ModelChoiceField(queryset=Webpage.objects.all())
    author = forms.CharField()
    