from django.shortcuts import render
from identifiant.models import *
from identifiant.forms import *
from django.views.generic import TemplateView,DeleteView,CreateView,ListView,DetailView,UpdateView
from .forms import *
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages 
from django.urls import reverse
from django.shortcuts import render,redirect

# Create your views here.

########DetailPatient
class DetailPatient(LoginRequiredMixin,DetailView):
    template_name="patient/DetailPatient.html"
    queryset=identitePatient.objects.all()
    context_object_name="Patient"    
#########list patient
class ListPatient(LoginRequiredMixin,ListView):
    template_name="patient/ListPatient.html"
    queryset=identitePatient.objects.all()
    context_object_name="Patient"
    def get_queryset(self):
        userprofile=self.request.user.userprofile
        return identitePatient.objects.filter(userprofile=userprofile)      
########updater le patient
class UpdatePatient(LoginRequiredMixin,UpdateView):
    template_name="patient/UpdatePatient.html"
    queryset=identitePatient.objects.all()
    form_class=updatePatientmodelForm
    def get_success_url(self):
        return reverse("patient:ListPatient")
######## Enregistrer le mail
def mail(request,pk):
    form=createMailform()
    if request.method=="POST":
        form=createMailform(request.POST)
        
        if form.is_valid():
            print("le form est ausi valide") 
            mail=form.cleaned_data['mail']
           
           # medecin=User.objects.get(username=request.user),
            patient=identitePatient.objects.get(id=pk)
          
            patient.Email=mail
            patient.save()
        else:
            print ("form is invalid")
            print(form.errors.as_data())    
            ####adresse permanent
            messages.error(request, "Error")
            context={
        "form":createMailform()
                 }
            return render(request,"patient/mailform.html",context)            
        return redirect("/patient/ListPatient/")
    context={
        "form":createMailform()
    }
    return render(request,"patient/mailform.html",context)  


  #########Information clinique
def InfoCliniqueform(request,pk):
    form=InfoCliniqueForm()
    if request.method=="POST":
        form=InfoCliniqueForm(request.POST)        
        if form.is_valid():
            print("le form est ausi valide")  
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
            
            infoclinique=InfoClinique.objects.create(
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


         # Associer au patient
            patient=identitePatient.objects.get(id=pk)
            patient.InfoClinique=infoclinique
            patient.save()
    
        else:
            print ("form is invalid")
            print(form.errors.as_data())    
            ####adresse permanent
            messages.error(request, "Error")
            context={
        "form":InfoCliniqueForm()
                 }
            return render(request,"patient/mailform.html",context)  
        return redirect("/patient/ListPatient/")
    context={
        "form":InfoCliniqueForm()
    }
    return render(request,"patient/mailform.html",context)  
########Information radiologique

def InfoRadiologiqueform(request,pk):
    form=InfoRadiologiqueForm()
    if request.method=="POST":
        form=InfoRadiologiqueForm(request.POST)        
        if form.is_valid():
            print("le form est ausi valide")    
            Opacités_nodulaires_pseudo_tumorales=form.cleaned_data[ 'Opacités_nodulaires_pseudo_tumorales']
            Atteinte_pulmonaire_unilatérale_Droite=form.cleaned_data['Atteinte_pulmonaire_unilatérale_Droite']
            Atteinte_pulmonaire_unilatérale_Gauche=form.cleaned_data[ 'Atteinte_pulmonaire_unilatérale_Gauche']
            Alvéolaire=form.cleaned_data['Alvéolaire']
            alveol_interstitielle=form.cleaned_data['alveol_interstitielle']
            Epanchement_pleuralRadiologique=form.cleaned_data['Epanchement_pleuralRadiologique']
            AutreInfoRadiologigue=form.cleaned_data['AutreInfoRadiologigue']
            inforadiologique=InfoRadiologique.objects.create(
                Opacités_nodulaires_pseudo_tumorales=Opacités_nodulaires_pseudo_tumorales,
                Atteinte_pulmonaire_unilatérale_Droite=Atteinte_pulmonaire_unilatérale_Droite,
                Atteinte_pulmonaire_unilatérale_Gauche=Atteinte_pulmonaire_unilatérale_Gauche,
                Alvéolaire=Alvéolaire,
                alveol_interstitielle=alveol_interstitielle,
                Epanchement_pleuralRadiologique=Epanchement_pleuralRadiologique,
                AutreInfoRadiologigue=AutreInfoRadiologigue,
            )           
           # Associer au user
            patient=identitePatient.objects.get(id=pk)
            patient.InfoRadiologique=inforadiologique
            patient.save()
        else:
            print ("form is invalid")
            print(form.errors.as_data())    
            ####adresse permanent
            messages.error(request, "Error")
            context={
        "form":InfoRadiologiqueForm()
                 }
            return render(request,"patient/mailform.html",context)  
        return redirect("/patient/ListPatient/")
    context={
        "form":InfoRadiologiqueForm()
    }
    return render(request,"patient/mailform.html",context)  
###########info biologique

def InfoBiologiqueform(request,pk):
    form=InfoBiologiqueForm()
    if request.method=="POST":
        form=InfoBiologiqueForm(request.POST)        
        if form.is_valid():
            print("le form est ausi valide")  

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

            infobiologique=InfoBiologique.objects.create(
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
         # Associer au user
            patient=identitePatient.objects.get(id=pk)
            patient.InfoBiologique=infobiologique
            patient.save()
        else:
            print ("form is invalid")
            print(form.errors.as_data())    
            ####adresse permanent
            messages.error(request, "Error")
            context={
        "form":InfoBiologiqueForm()
                 }
            return render(request,"patient/mailform.html",context)  
        return redirect("/patient/ListPatient/")
    context={
        "form":InfoBiologiqueForm()
    }
    return render(request,"patient/mailform.html",context)      


#### QuestionAvecPrelevementForm
def QuestionAvecPrelevementform(request,pk):
    form=QuestionAvecPrelevementForm()
    if request.method=="POST":
        form=QuestionAvecPrelevementForm(request.POST)        
        if form.is_valid():
            print("le form est ausi valide")  
            Liquide_de_ponction_pleurale=form.cleaned_data['Liquide_de_ponction_pleurale']
            Crachats=form.cleaned_data['Crachats']
            Liquides_d_aspirations=form.cleaned_data['Liquides_d_aspirations']
            Lavage_broncho_pulmonaires=form.cleaned_data['Lavage_broncho_pulmonaires']
            Urines=form.cleaned_data['Urines']
            Sang=form.cleaned_data['Sang']    
            AutrePrelevement=form.cleaned_data['AutrePrelevement']
            questionavecprelevement=QuestionAvecPrelevement.objects.create(
                Liquide_de_ponction_pleurale=Liquide_de_ponction_pleurale,
                Crachats=Crachats,
                Liquides_d_aspirations=Liquides_d_aspirations,
                Lavage_broncho_pulmonaires=Lavage_broncho_pulmonaires,
                Urines=Urines,
                Sang=Sang,
                AutrePrelevement=AutrePrelevement,
            )
            # Associer au patient
            patient=identitePatient.objects.get(id=pk)
            patient.QuestionAvecPrelevement=questionavecprelevement
            patient.save()
    
        else:
            print ("form is invalid")
            print(form.errors.as_data())    
            ####adresse permanent
            messages.error(request, "Error")
            context={
        "form":QuestionAvecPrelevementForm()
                 }
            return render(request,"patient/mailform.html",context)  
        return redirect("/patient/ListPatient/")
    context={
        "form":QuestionAvecPrelevementForm()
    }
    return render(request,"patient/mailform.html",context)      

       