from django import http, urls
from django.contrib import admin
from django.urls import path
from .views import DetailMedecin, homepage,create,signup,ListMedecin, signup, updateUser
from django.contrib.auth.views import LoginView,LogoutView


app_name="identifiant"

urlpatterns = [
    path('',homepage,name="homepage"),
    path('ListMedecin/',ListMedecin.as_view(),name="ListMedecin"),
    path('<int:pk>/',DetailMedecin.as_view(),name="detail"),
     #path('hi/',hi,name="page"),
     #path('create/',ccreate.as_view(),name="ccreate"), 
    
    path('<int:pk>/updateUser/',updateUser.as_view(),name="updateUser"), 
    path('create/',create,name="create"), 
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('signup/',signup,name="signup"), 
]