from django import http, urls
from django.contrib import admin
from django.urls import path
from .views import DetailMedecin, DeleteMedecin,  homepage,ValiderMedecin,create,signup,ListMedecin, signup, updateUser
from django.contrib.auth.views import LoginView,LogoutView


app_name="identifiant"

urlpatterns = [
    path('',homepage,name="homepage"),
    path('ListMedecin/',ListMedecin.as_view(),name="ListMedecin"),
   # path('ListPatient/',ListPatient.as_view(),name="ListPatient"),
    path('<int:pk>',DetailMedecin.as_view(),name="DetailMedecin"),
    ########patient
   # path('<int:pk>/DetailPatient/',DetailPatient.as_view(),name="DetailPatient"),

    path('<int:pk>/ValiderMedecin',ValiderMedecin,name="ValiderMedecin"),

    path('<int:pk>/DeleteMedecin/',DeleteMedecin.as_view(),name="DeleteMedecin"),
    
    
   
   
    #path('create/',ccreate.as_view(),name="ccreate"), 
    
    path('<int:pk>/updateUser/',updateUser.as_view(),name="updateUser"), 
    path('create/',create,name="create"), 
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path('signup/',signup,name="signup"), 
]