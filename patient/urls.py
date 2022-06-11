from django import http, urls
from django.contrib import admin
from django.urls import path
from .views import  DetailPatient, InfoCliniqueform, ListPatient, QuestionAvecPrelevementform, UpdatePatient,mail,InfoRadiologiqueform,QuestionAvecPrelevementform,InfoBiologiqueform
from django.contrib.auth.views import LoginView,LogoutView


app_name="patient"

urlpatterns = [
    #path('',homepage,name="homepage"),
   
    path('ListPatient/',ListPatient.as_view(),name="ListPatient"),
   
 
    path('<int:pk>',DetailPatient.as_view(),name="DetailPatient"),

    path('<int:pk>/UpdatePatient/',UpdatePatient.as_view(),name="UpdatePatient"),

    path('<int:pk>/mail',mail,name="MailPatient"),
    path('<int:pk>/InfoClinique',InfoCliniqueform,name="InfoClinique"),  
    path('<int:pk>/InfoRadiologique',InfoRadiologiqueform,name="InfoRadiologique"), 
    path('<int:pk>/InfoBiologique',InfoBiologiqueform,name="InfoBiologique"),
    path('<int:pk>/QuestionAvecPrelevement',QuestionAvecPrelevementform,name="QuestionAvecPrelevement"), 

    #path('<int:pk>/DeleteMedecin/',DeleteMedecin.as_view(),name="DeleteMedecin"),
    
    
   
   
    #path('create/',ccreate.as_view(),name="ccreate"), 
    
    #path('<int:pk>/updateUser/',updateUser.as_view(),name="updateUser"), 
   # path('create/',create,name="create"), 
   
]