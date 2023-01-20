from django.http import HttpResponse
from django.shortcuts import render

from datetime import datetime

def index(request):
    return render(request, "index.html")

#def afficher_login(request):
 #   return render(request, "registration/login.html")

def _medecin(request):
    return render(request, "medecin.html")

def _formulaire(request):
    return render(request, "Ajout_patient.html")

def _details(request):
    return render(request, "Details_patient.html")