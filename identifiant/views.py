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
    
def hi(request):
    return render(request,"identifiant/h.html")
####LIste des medecin
class ListMedecin(ListView):
    template_name="identifiant/ListMedecin.html"
    queryset=User.objects.all()
    context_object_name="Medecin"
#####DetailMedecin
class DetailMedecin(DetailView):
    template_name="identifiant/DetailMedecin.html"
    queryset=User.objects.all()
    context_object_name="Medecin"   
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


        #######2-Information clinique###
            Fievre=form.cleaned_data["Fievre"]
            Lethargie=form.cleaned_data["Lethargie"]
            Myalgies_arthralgies=form.cleaned_data["Myalgies_arthralgies"]
            Cephalees=form.cleaned_data["Cephalees"]
            Tachycardie=form.cleaned_data["Tachycardie"]
            Polypnee=form.cleaned_data["Polypnee"]
            TouxSeche=form.cleaned_data["TouxSeche"]
            TouxProductive=form.cleaned_data["TouxProductive"]
            TouxPurulente=form.cleaned_data["TouxPurulente"]
            DouleurThoracique=form.cleaned_data["DouleurThoracique"]
           
            Dyspnee=form.cleaned_data["Dyspnee"]
            DefaillanceRespiratoire=form.cleaned_data["DefaillanceRespiratoire"]
            Confusion=form.cleaned_data["Confusion"]
            Diarrhees=form.cleaned_data["Diarrhees"]
           
            Vomissements=form.cleaned_data["Vomissements"]
            Douleurs_abdominales=form.cleaned_data["Douleurs_abdominales"]
            Epanchement_pleuralClinique=form.cleaned_data["Epanchement_pleuralClinique"]
            AutreInfoClinique=form.cleaned_data["AutreInfoClinique"]
            
            InfoClinique1=InfoClinique.objects.create(
                Fievre=Fievre,
                Lethargie=Lethargie,
                Myalgies_arthralgies=Myalgies_arthralgies,
                Cephalees=Cephalees,
                Tachycardie=Tachycardie,
                Polypnee=Polypnee,
                TouxSeche=TouxSeche,
                TouxProductive=TouxProductive,
                TouxPurulente=TouxPurulente,
                DouleurThoracique=DouleurThoracique,
                Dyspnee=Dyspnee,
                DefaillanceRespiratoire=DefaillanceRespiratoire,
                Confusion=Confusion,
                Diarrhees=Diarrhees,
                Vomissements=Vomissements,
                Douleurs_abdominales=Douleurs_abdominales,
                Epanchement_pleuralClinique= Epanchement_pleuralClinique,
                AutreInfoClinique=AutreInfoClinique,
            )
        ########3-Information radiologique ### 
            Opacités_nodulaires_pseudo_tumorales=form.cleaned_data["Opacités_nodulaires_pseudo_tumorales"]
            Atteinte_pulmonaire_unilatérale_Droite=form.cleaned_data["Atteinte_pulmonaire_unilatérale_Droite"]
            Atteinte_pulmonaire_unilatérale_Gauche=form.cleaned_data["Atteinte_pulmonaire_unilatérale_Gauche"]
            Alvéolaire=form.cleaned_data["Alvéolaire"]
            alveol_interstitielle=form.cleaned_data["alveol_interstitielle"]
            Epanchement_pleuralRadiologique=form.cleaned_data["Epanchement_pleuralRadiologique"]
            AutreInfoRadiologigue=form.cleaned_data["AutreInfoRadiologigue"]
            
            InfoRadiologique1=InfoRadiologique.objects.create(
                Opacités_nodulaires_pseudo_tumorales=Opacités_nodulaires_pseudo_tumorales,
                Atteinte_pulmonaire_unilatérale_Droite=Atteinte_pulmonaire_unilatérale_Droite,
                Atteinte_pulmonaire_unilatérale_Gauche=Atteinte_pulmonaire_unilatérale_Gauche,
                Alvéolaire=Alvéolaire,
                alveol_interstitielle=alveol_interstitielle,
                Epanchement_pleuralRadiologique=Epanchement_pleuralRadiologique,
                AutreInfoRadiologigue=AutreInfoRadiologigue,
            )
        ########4-Information Biologique ### 
            CRP=form.cleaned_data["CRP"]
            Pro_calcitonine=form.cleaned_data["Pro_calcitonine"]
            Albuminémie=form.cleaned_data["Albuminémie"]
            Ferritine=form.cleaned_data["Ferritine"] 
            Sélenium=form.cleaned_data["Sélenium"]
            Phosphorémie=form.cleaned_data["Phosphorémie"]
            Pao2=form.cleaned_data["Pao2"]
            LDH=form.cleaned_data["LDH"]
            Tx_de_Globules_blancs=form.cleaned_data["Tx_de_Globules_blancs"]
            Tx_de_plaquettes =form.cleaned_data["Tx_de_plaquettes"]
            Tx_de_lymphocytes =form.cleaned_data["Tx_de_lymphocytes"]
            SGPT=form.cleaned_data["SGPT"]
            SGOT=form.cleaned_data["SGOT"]
            Bilirubine=form.cleaned_data["Bilirubine"]
            Phosphatases_alcalines =form.cleaned_data["Phosphatases_alcalines"]
            Urée=form.cleaned_data["Urée"]
            Créatinémie=form.cleaned_data["Créatinémie"]
            Natrémie=form.cleaned_data["Natrémie"]
            Kaliémie=form.cleaned_data["Kaliémie"]
            Proteinurie=form.cleaned_data["Proteinurie"]
            Hématurie=form.cleaned_data["Hématurie"]
            CPK=form.cleaned_data["CPK"]

            InfoBiologique1=InfoBiologique.objects.create(
                CRP=CRP,
                Pro_calcitonine=Pro_calcitonine,
                Albuminémie=Albuminémie,
                Ferritine=Ferritine,
                Sélenium=Sélenium,
                Phosphorémie=Phosphorémie,
                Pao2=Pao2,
                LDH=LDH,
                Tx_de_Globules_blancs=Tx_de_Globules_blancs,
                Tx_de_plaquettes=Tx_de_plaquettes,
                Tx_de_lymphocytes=Tx_de_lymphocytes,
                SGPT=SGPT,
                SGOT=SGOT,
                Bilirubine=Bilirubine,
                Phosphatases_alcalines=Phosphatases_alcalines,
                Urée=Urée,
                Créatinémie=Créatinémie,
                Natrémie=Natrémie,
                Kaliémie=Kaliémie,
                Proteinurie=Proteinurie,
                Hématurie=Hématurie,
                CPK=CPK,
                
            )
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
        ########7-Question avec prelevement###   
            Liquide_de_ponction_pleurale=form.cleaned_data["Liquide_de_ponction_pleurale"]
            Crachats=form.cleaned_data["Crachats"]
            Liquides_d_aspirations=form.cleaned_data["Liquides_d_aspirations"]
            Lavage_broncho_pulmonaires=form.cleaned_data["Lavage_broncho_pulmonaires"]
            Urines=form.cleaned_data["Urines"]
            Sang=form.cleaned_data["Sang"]
            AutrePrelevement=form.cleaned_data["AutrePrelevement"]

            QuestionAvecPrelevement1=QuestionAvecPrelevement.objects.create(
                Liquide_de_ponction_pleurale=Liquide_de_ponction_pleurale,
                Crachats=Crachats,
                Liquides_d_aspirations=Liquides_d_aspirations,
                Lavage_broncho_pulmonaires=Lavage_broncho_pulmonaires,
                Urines=Urines,
                Sang=Sang,
                AutrePrelevement=AutrePrelevement,
            )



              
               
             


            formulaire.objects.create(
                Date_Introduction=Date_Introduction,
                patientvu=patientvu,
                identitePatient=patient,
                medecin=User.objects.get(username=request.user),
                etatDuPatient=etatDuPatient,
                DiagnosticDepathologiChronique=DiagnosticDepathologiChronique,
                SipathologieChroniqueAso=SipathologieChroniqueAso,
                facteurRisque=facteurRisque1,
                Therapieimmunosuppressiveencours=Therapieimmunosuppressiveencours1,
                InfoClinique=InfoClinique1,
                InfoRadiologique=InfoRadiologique1,
                InfoBiologique=InfoBiologique1,
                traitementRecu=traitementRecu1,
                InfoSupDunEntourage=InfoSupDunEntourage,
                QuestionAvecPrelevement=QuestionAvecPrelevement1,

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
