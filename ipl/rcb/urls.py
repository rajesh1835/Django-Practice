from django.urls import path
from .views import *

app_name = "SomethingSomething"

urlpatterns = [
    path("captain/", captain, name="captain"),
    path("viceCaptain/", viceCaptain, name="viceCaptain"),
]