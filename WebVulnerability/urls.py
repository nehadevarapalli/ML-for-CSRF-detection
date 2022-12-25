"""WebVulnerability URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from WebVulnerability import views as mainView
from users import views as usr
from admins import views as admins
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("index/", mainView.logout, name="index"),
    path("", mainView.index, name="index"),
    path("logout/", mainView.logout, name="logout"),
    path("UserLogin/", mainView.UserLogin, name="UserLogin"),
    path("AdminLogin/", mainView.AdminLogin, name="AdminLogin"),
    path("UserRegister/", mainView.UserRegister, name="UserRegister"),

    #### User Views #####
    path("UserRegisterActions/", usr.UserRegisterActions, name="UserRegisterActions"),
    path("UserLoginCheck/", usr.UserLoginCheck, name="UserLoginCheck"),
    path("UserHome/",usr.UserHome, name="UserHome"),
    path("UserPreProcessForm/", usr.UserPreProcessForm, name="UserPreProcessForm"),
    path("UserCSRFProcessByBolt/", usr.UserCSRFProcessByBolt, name="UserCSRFProcessByBolt"),
    path("UserMitchProcess/", usr.UserMitchProcess, name="UserMitchProcess"),
    path("UserMachineLearning/", usr.UserMachineLearning, name="UserMachineLearning"),



    #####Admin Side Views #######
    path("AdminLoginCheck/", admins.AdminLoginCheck, name="AdminLoginCheck"),
    path("AdminHome/", admins.AdminHome, name="AdminHome"),
    path("AdminViewUsers/", admins.AdminViewUsers, name="AdminViewUsers"),
    path("AdminActivaUsers/", admins.AdminActivaUsers, name="AdminActivaUsers"),
    path("adminviewallcsrfs/", admins.adminviewallcsrfs, name="adminviewallcsrfs"),
    path("PostRequestdata/", admins.PostRequestdata, name="PostRequestdata"),
    path("GetRequestdata/", admins.GetRequestdata, name="GetRequestdata"),




]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
