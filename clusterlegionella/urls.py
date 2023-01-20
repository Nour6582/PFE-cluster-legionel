"""clusterlegionella URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from argparse import Namespace
from django import urls

from django.contrib import admin
from django.urls import path,include

from .views import index, _medecin, _formulaire, _details #afficher_login,
from patient.views import ListPatient
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [

#    path('login', afficher_login, name="login"),

  

    path('medecin',ListPatient.as_view(), name="medecin"),

    path('formulaire', _formulaire, name="formulaire"),

    path('patient', _details, name="patient"),

    path('',index, name="monindex"),

    path('admin/', admin.site.urls),

    path('identifiant/',include('identifiant.urls',namespace="identifiant")),
     path('patient/',include('patient.urls',namespace="patient")),

]
