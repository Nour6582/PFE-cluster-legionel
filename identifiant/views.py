from xml.dom.minidom import Identified
from django.urls import reverse
from multiprocessing import context
from re import T, template
from typing import Generic
from urllib import request
from django import conf
from django.shortcuts import render,redirect
from django.views import generic
from django.views.generic import TemplateView,DeleteView,CreateView,ListView,DetailView,UpdateView
from .forms import *
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages 
from .models import User
# Create your views here.


def signup(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'registration/signup.html', context={'form': form})




def homepage(request):
    mes="hello it's homepage"
    context= {  'mes':mes }
    return render(request,"identifiant/homepage.html",context)
    

####Liste des medecin
class ListMedecin(LoginRequiredMixin,ListView):
    template_name="identifiant/ListMedecin.html"
    queryset=User.objects.all()
    context_object_name="Medecin"

#####DetailMedecin
class DetailMedecin(LoginRequiredMixin,DetailView):
    template_name="identifiant/DetailMedecin.html"
    queryset=User.objects.all()
    context_object_name="med"   

#########DeleteMedecin
class DeleteMedecin(LoginRequiredMixin,DeleteView):
    template_name="identifiant/DeleteMedecin.html"
    queryset=User.objects.all()
    context_object_name="Medecin" 
    def get_success_url(self) :
        return reverse("identifiant:ListMedecin")
######validateMedecin
def ValiderMedecin(request,pk):
    Medecin=User.objects.get(id=pk)
    Medecin.is_Medecin=True
    Medecin.is_attente=False
    Medecin.save()
    return redirect("identifiant:ListMedecin")
        

#########update du medecin    
class updateUser(LoginRequiredMixin,UpdateView):
    template_name="identifiant/updateUser.html"
    queryset=User.objects.all()
    form_class=updateUsermodelForm
    def get_success_url(self):
        return reverse("identifiant:login")
    





def create(request):
    form=createform()
    if request.method=="POST":
        form=createform(request.POST)
        
        if form.is_valid():
            print("le form est ausi valide") 
         ######Gerer la creation de compte du patient###
            ####le lieu de naissance
            wilaya=form.cleaned_data['wilaya']
            Daira=form.cleaned_data['Daira']
            Commune=form.cleaned_data['Commune']      
            #existe=lieu.objects.filter(wilaya=wilaya,Daira=Daira,Commune=Commune)
            lieu_1=lieu.objects.filter(
                wilaya=wilaya,
                Daira=Daira,
                Commune=Commune,
            )
            if not lieu_1:
                lieu_naissance=lieu.objects.create(
                wilaya=wilaya,
                Daira=Daira,
                Commune=Commune,
            )
            else:
                lieu_naissance=lieu_1[0]
            ####lieu de residence
            adressewilaya=form.cleaned_data['adressewilaya']
            adresseDaira=form.cleaned_data['adresseDaira']
            adresseCommune=form.cleaned_data['adresseCommune']

            lieu_residence1=lieu.objects.filter(
            wilaya=adressewilaya,
            Daira=adresseDaira,
            Commune=adresseCommune,
           )
            if not lieu_residence1:
                lieu_residence=lieu.objects.create(
                    wilaya=adressewilaya,
                    Daira=adresseDaira,
                    Commune=adresseCommune,
                )
            else:
                lieu_residence=lieu_residence1[0]    

            NumRue=form.cleaned_data['NumRue']
            NomRue=form.cleaned_data['NomRue']
            CodePostal=form.cleaned_data['CodePostal']
            NumBoitePostal=form.cleaned_data['NumBoitePostal']
            NumBattiment=form.cleaned_data['NumBattiment']
            NumAppartement=form.cleaned_data['NumAppartement']
           
            ResidencePermanent= adresseResidence.objects.create(
                NumRue=NumRue,
                NomRue=NomRue,
                CodePostal=CodePostal,
                NumBoitePostal=NumBoitePostal,
                NumBattiment=NumBattiment,
                NumAppartement=NumAppartement,
                adresse=lieu_residence,
            )

            Nom=form.cleaned_data['Nomp']
            NomMarital=form.cleaned_data['Nommaritalp']
            Prenom=form.cleaned_data['Prenomp']
            
            #agent=lead.objects.first()
            sexe=form.cleaned_data['sexe']
            Date_naissance=form.cleaned_data['datenaissance']
            
            Tel=form.cleaned_data['Tel']
            fax=form.cleaned_data['fax']
            Email=form.cleaned_data['Email']


#            userprofile=self.request.user.userprofile
#        return identitePatient.objects.filter(userprofile=userprofile) 
           ####medecin introducteur d'info

            medecin1=User.objects.get(username=request.user),

            medecin=medecin1[0]
            patient=identitePatient.objects.create(
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
                userprofile=medecin.userprofile,
            
            ) 


         ######Gerer la creation de compte de l'introducteur d'info###
            
         ######Gerer la creation du formulaire###




            Date_Introduction=form.cleaned_data['Date_Introduction']
            patientvu=form.cleaned_data["patientvu"]


        ######1-Etat du patient au moment de l'introduction de l'information###
            etatDuPatient=form.cleaned_data["etatDuPatient"]
            DiagnosticDepathologiChronique=form.cleaned_data["DiagnosticDepathologiChronique"]
            SipathologieChroniqueAso=form.cleaned_data["SipathologieChroniqueAso"]
        
        
        ######facteur Risque
                
                
            facteurrisque=form.cleaned_data["facteurrisque"]


            if 'Greffe de Moelle osseuse' in facteurrisque:
                GreffedeMoelleosseuse='Greffe de Moelle osseuse'
            else:
                GreffedeMoelleosseuse =''

            if     'Greffe de rein' in facteurrisque:
                Greffederein='Greffe de rein'
            else:
                Greffederein=''

            if 'Splenectomie' in facteurrisque:
                Splenectomie='Splenectomie'
            else:
                Splenectomie=''  

            if   'Tabac' in facteurrisque:
                Tabac='Tabac'
            else:
                Tabac=''  



            facRisque=facteurRisque.objects.filter(
                GreffedeMoelleosseuse=GreffedeMoelleosseuse,
                Greffederein=Greffederein,
                Splenectomie=Splenectomie,
                Tabac=Tabac,
            ) 


             #facteurRisque
            if not facRisque:
                facteurRisque1=facteurRisque.objects.create(
                GreffedeMoelleosseuse=GreffedeMoelleosseuse,
                Greffederein=Greffederein,
                Splenectomie=Splenectomie,
                Tabac=Tabac,
            )    
            else:
                facteurRisque1=facRisque[0]


     #Si Thérapie immunosuppressive en cours, préciser

     
            #######si Thérapie immunosuppressive en cours, 
            Typetherapie=form.cleaned_data["Typetherapie"]
            
            if 'chimiothérapie' in Typetherapie:
                chimiothérapie='chimiothérapie'
            else:
                chimiothérapie=''    
            ##############
            if 'anti-TNF alpha' in Typetherapie:
                anti_TNFalpha='anti-TNF alpha'
            else:
                anti_TNFalpha=''
            ###########
            if 'Corticothérapie'  in Typetherapie:
                Corticothérapie='Corticothérapie' 
            else:
                Corticothérapie=''    

            typether=Therapieimmunosuppressiveencours.objects.filter(
                chimiothérapie=chimiothérapie,
                anti_TNFalpha=anti_TNFalpha,
                Corticothérapie=Corticothérapie,
            )   

            if not typether:
               Therapieimmunosuppressiveencours1=Therapieimmunosuppressiveencours.objects.create(
                chimiothérapie=chimiothérapie,
                anti_TNFalpha=anti_TNFalpha,
                Corticothérapie=Corticothérapie,
            )   
            else:
                Therapieimmunosuppressiveencours1=typether[0]


        
        ########5-Autre traitement recu ### 
            traitementEncours=form.cleaned_data["traitementEncours"]
            traitementAvantConsultation=form.cleaned_data["traitementAvantConsultation"]
            AutreTraitementimmunosuppresseur=form.cleaned_data["AutreTraitementimmunosuppresseur"]

            traitementRecu1=traitementRecu.objects.create(
                traitementEncours=traitementEncours,
                traitementAvantConsultation=traitementAvantConsultation,
                AutreTraitementimmunosuppresseur=AutreTraitementimmunosuppresseur,
            )

         ########6-coordonner de quelquun sup ### 
            InfoSupDunEntourage=form.cleaned_data["InfoSupDunEntourage"]    
        


              
               
             


            formulaire.objects.create(
                Date_Introduction=Date_Introduction,
                patientvu=patientvu,
                identitePatient=patient,
                medecin=medecin,
                etatDuPatient=etatDuPatient,
                DiagnosticDepathologiChronique=DiagnosticDepathologiChronique,
                SipathologieChroniqueAso=SipathologieChroniqueAso,
                facteurRisque=facteurRisque1,
                Therapieimmunosuppressiveencours=Therapieimmunosuppressiveencours1,
               
                traitementRecu=traitementRecu1,
                InfoSupDunEntourage=InfoSupDunEntourage,
           

            )    
        else:
            print ("form is invalid")
            print(form.errors.as_data())    
            ####adresse permanent
            messages.error(request, "Error")
            context={
        "form":createform()
                 }
            return render(request,"identifiant/formulaire1.html",context)  
            

           
        return redirect("/identifiant/")
    context={
        "form":createform()
    }
    return render(request,"identifiant/formulaire1.html",context)  


