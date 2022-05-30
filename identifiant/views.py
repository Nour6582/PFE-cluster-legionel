from audioop import reverse
from multiprocessing import context
from re import T, template
from typing import Generic
from urllib import request
from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import TemplateView,DeleteView,CreateView,ListView,DetailView,UpdateView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages 
# Create your views here.
class signup(generic.CreateView):
    template_name="registration/signup.html"
    form_class=CustomUserCreationForm
    def get_success_url(self):
        return "login"

def homepage(request):
    mes="hello it's homepage"
    context= {  'mes':mes }
    return render(request,"identifiant/h.html",context)
    
def hi(request):
    return render(request,"identifiant/h.html")



class ccreate(CreateView):
    template_name="identifiant/create.html"
    form_class=createmodelForm
    def get_success_url(self):
        return "/identifiant/"



def create(request):
    form=createform()
    if request.method=="POST":
        form=createform(request.POST)
        
        if form.is_valid():
            print("le form est ausi valide") 
            ####le lieu de naissance
            Wilaya=form.cleaned_data['Wilaya']
            Daira=form.cleaned_data['Daira']
            Commune=form.cleaned_data['Commune']
            lieu_naissance=lieu.objects.create(
                Wilaya=Wilaya,
                Daira=Daira,
                Commune=Commune,
            )
            NumRue=form.cleaned_data['NumRue']
            NomRue=form.cleaned_data['NomRue']
            CodePostal=form.cleaned_data['CodePostal']
            NumBoitePostal=form.cleaned_data['NumBoitePostal']
            NumBattiment=form.cleaned_data['NumBattiment']
            NumAppartement=form.cleaned_data['NumAppartement']
            adresseWilaya=form.cleaned_data['adresseWilaya']
            adresseDaira=form.cleaned_data['adresseDaira']
            adresseCommune=form.cleaned_data['adresseCommune']
            ResidencePermanent= adresseResidence.objects.create(
                NumRue=NumRue,
                NomRue=NomRue,
                CodePostal=CodePostal,
                NumBoitePostal=NumBoitePostal,
                NumBattiment=NumBattiment,
                NumAppartement=NumAppartement,
                adresseWilaya=adresseWilaya,
                adresseDaira=adresseDaira,
                adresseCommune=adresseCommune,
            )

            Nom=form.cleaned_data['Nomp']
            NomMarital=form.cleaned_data['Nommaritalp']
            Prenom=form.cleaned_data['Prenom']
            
            #agent=lead.objects.first()
            sexe=form.cleaned_data['sexe']
            Date_naissance=form.cleaned_data['datenaissance']
            
            Tel=form.cleaned_data['Tel']
            fax=form.cleaned_data['fax']
            Email=form.cleaned_data['Email']

           

            identitePatient.objects.create(
                Nom=Nom,
                NomMarital=NomMarital,
                Prenom=Prenom,
                sexe=sexe,
                Date_naissance=Date_naissance,
                lieu_naissance=lieu_naissance,
                Tel=Tel,
                fax=fax,
                Email=Email,
                ResidencePermanent=ResidencePermanent,
            
            ) 
        else:
            print ("form is invalid")
            print(form.errors.as_data())    
            ####adresse permanent
            messages.error(request, "Error")
            context={
        "form":createform()
                 }
            return render(request,"identifiant/create.html",context)  
            

           
        return redirect("/identifiant/")
    context={
        "form":createform()
    }
    return render(request,"identifiant/create.html",context)  

#class ccreate(LoginRequiredMixin,CreateView):
    template_name="identifiant/create.html"
    form_class=createmodelForm
    def get_success_url(self):
        return reverse('indentifiant/h.html')
