from django import http, urls
from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView


app_name="identifiant"

urlpatterns = [
    path('',homepage,name="homepage"),
     path('hi/',hi,name="page"),
     #path('create/',ccreate.as_view(),name="ccreate"), 
    path('create/',create,name="create"), 
     path('login/',LoginView.as_view(),name="login"),
      path('logout/',LogoutView.as_view(),name="logout"),
      path('signup/',signup.as_view(),name="signup"), 
]