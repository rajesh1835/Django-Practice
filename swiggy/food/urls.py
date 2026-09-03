from django.urls import path
from .views import *

app_name="food"

urlpatterns = [
    path("home/", home, name="home"),
    path("biryani/", biryani, name="biryani"),
    path("dosa/", dosa, name="dosa"),
]
