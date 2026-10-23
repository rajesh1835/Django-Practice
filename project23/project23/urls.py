"""
URL configuration for project23 project.

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
from django.urls import path
from accounts.views import create_user, bombit, user_login, home, user_logout, display_details, change_password, reset_password
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", create_user, name="create-user"),
    path("bomb/", bombit, name="bombit"),
    path("", home, name="home"),
    path("user_login/", user_login, name="user-login"),
    path("user_logout/", user_logout, name="user-logout"),
    path("display_details/", display_details, name="display-details"),
    path("change_password/", change_password, name="change-password"),
    path("reset_password/", reset_password, name="reset-password"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
