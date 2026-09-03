from django.urls import path
from .views import *

app_name = "instamart"

urlpatterns = [ 
    path("home/", home, name="home"),
    path("icecream/", ice_cream, name="icecream"),
    path("biscuits/", biscuits, name="biscuits"), 
]