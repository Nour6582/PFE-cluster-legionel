from argparse import ArgumentError
from email.policy import default
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,UsernameField

from django.contrib.auth import get_user_model
from django import forms
from .models import *
from identifiant.models import introducteurDinfo

User= get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}



choixlieu= ( 
    ('hospitalisation','hospitalisation'),
    ('HDJ','HDJ'),
    ('Consultation','Consultation en dehors de CPU'),
    ('PU','PU'), )

sexe=(
   ('M','M'),
   ('F','F'),
)      
Etat=(
    ('Gueri','Gueri'),
    ('Malade','Malade'),
    ('Decede','Decede'),
)



Therapie=(
    ('chimiothérapie','chimiothérapie'),
    ('anti-TNF alpha','anti-TNF alpha'),
    ('Corticothérapie','Corticothérapie'),
  
)
facteurdeRisque=(
    ('Greffe de Moelle osseuse','Greffe de Moelle osseuse'),
    ('Greffe de rein','Greffe de rein'),
    ('Splenectomie','Splenectomie'),
    ('Tabac','Tabac'),
)
Reponse =(
        ('Oui','Oui'),
        ('Je ne sais pas','Je ne sais pas'),
)

class createform(forms.Form):
    Date_Introduction=forms.DateField(label='  Date d’introduction du questionnaire ')
    patientvu=forms.ChoiceField(label='Patient ( e ) vu ( e )',choices=choixlieu)
  
    
    
    #identite du patient
    ########
    #######
    #########
    #######
    #######
    #######

    Nomp=forms.CharField(label='Nom (de jeune fille si femme)',max_length=30)
    Nommaritalp=forms.CharField(label='Nom marital ( si femme) ',max_length=30,required=False)
    Prenomp=forms.CharField(label='Prénom (s) ',max_length=30)
    datenaissance=forms.DateField(label='Date de naissance ')
    sexe=forms.ChoiceField(choices=sexe)
    Tel=forms.IntegerField(label='Tel (fixe et/ou/portable) ')
    fax=forms.IntegerField()
    Email=forms.EmailField()
    #lieu de naissance du patient
    wilaya=forms.CharField() 
    Daira=forms.CharField() 
    Commune=forms.CharField() 
    #adresse de residence permanente du patient
    NumRue=forms.IntegerField(label="Numero de la Rue")
    NomRue=forms.CharField(label="Nom de la Rue",max_length=100)
    CodePostal=forms.IntegerField(label="Code Postal")
    NumBoitePostal=forms.IntegerField(label="Numero de la boite  postale ( si c’est la cas) ",required=False)
    NumBattiment=forms.IntegerField(label="Numéro de la maison ou du bâtiment ")
    NumAppartement=forms.IntegerField(label="Numéro de l’appartement, si c’est le cas ",required=False)
    adressewilaya=forms.CharField(label='Wilaya') 
    adresseDaira=forms.CharField(label='Daira') 
    adresseCommune=forms.CharField(label='Commune') 
   
    
     #Le medecin qui introduit les donner
    ########
    #######
    #########
    #######
    #######
    #######
    NomMedecin=forms.CharField(label='Nom du Medecin',max_length=30)
    PrenomMedecin=forms.CharField(label='Prenom du Medecin',max_length=30)
    EmailMedecin=forms.EmailField(label='Email du Medecin')
    telPortableMedecin=forms.IntegerField(label='Tel portable')
    telMedecin=forms.IntegerField(label='telephone du Medecin')
    faxMedecin=forms.IntegerField(label='fax du Medecin')
     #Formulaire
    ########
    #######
    #########
    #######
    #######
    #######
     ####information sur etat du patient au moment de lintroduction du questionnaire

    etatDuPatient=forms.ChoiceField(label="Etat du patient (e) au moment de l’introduction du questionnaire",choices=Etat)
    DiagnosticDepathologiChronique=forms.CharField(label="Diagnostic de pathologie chronique ",max_length=9999999)
    SipathologieChroniqueAso=forms.CharField(label="Si Pathologie chronique associée",max_length=9999999)
    #fateur risque
    facteurrisque=forms.MultipleChoiceField(label="Facteurs de risque",choices=facteurdeRisque,widget=forms.CheckboxSelectMultiple,required=False)
    #si therapie en cours
    Typetherapie=forms.MultipleChoiceField(label="Si Thérapie immunosuppressive en cours, préciser",choices=Therapie,widget=forms.CheckboxSelectMultiple,required=False)
   

    #Informations cliniques du patient
    Lethargie=forms.ChoiceField(label="Léthargie",choices=Reponse)
    Myalgies_arthralgies=forms.ChoiceField(label="Myalgie/arthralgie",choices=Reponse)
    Cephalees=forms.ChoiceField(label="Céphalées",choices=Reponse)
    Tachycardie=forms.ChoiceField(label="Tachycardie (>ou=100/mn)", choices=Reponse)
    Diarrhees=forms.ChoiceField(label="Diarrhée", choices=Reponse)
    Vomissements=forms.ChoiceField(label="Vomissements", choices=Reponse)
    Douleurs_abdominales =forms.ChoiceField(label="Douleurs abdominales", choices=Reponse)
    Epanchement_pleuralClinique=forms.ChoiceField(label="Epanchement pleural", choices=Reponse)
                                #######
    DouleurThoracique=forms.ChoiceField(label="Douleur Thoracique", choices=Reponse) 
    Dyspnee=forms.ChoiceField(label="Dyspnée", choices=Reponse)
                            #######
    DefaillanceRespiratoire=forms.ChoiceField(label="Défaillance respiratoire", choices=Reponse)
    Polypnee=forms.ChoiceField(label="Polypnée (>ou=30/mn)", choices=Reponse)
    Confusion=forms.ChoiceField(label="Confusion",choices=Reponse)
    Fievre=forms.ChoiceField(label="Fièvre à Préciser",choices=Reponse)
    TouxSeche=forms.ChoiceField(label="Toux seche",choices=Reponse)
    TouxProductive=forms.ChoiceField(label="Toux Productive",choices=Reponse)
    TouxPurulente=forms.ChoiceField(label="Toux Purulente",choices=Reponse)
    AutreInfoClinique=forms.CharField(label="Autre",max_length=999999999,required=False)
    #Informations radiologiques, si elles sont disponibles :(cocher uniquement ce qui correspond à votre malade)
    Opacités_nodulaires_pseudo_tumorales=forms.ChoiceField(label="Opacités nodulaires pseudo- tumorales", choices=Reponse)
    Atteinte_pulmonaire_unilatérale_Droite=forms.ChoiceField(label="Atteinte pulmonaire unilatérale Droite", choices=Reponse)
    Atteinte_pulmonaire_unilatérale_Gauche=forms.ChoiceField(label="Atteinte pulmonaire unilatérale Gauche", choices=Reponse)
    Alvéolaire=forms.ChoiceField(label="Alvéolaire", choices=Reponse)
                            #####
    alveol_interstitielle=forms.ChoiceField(label="Atteinte pulmonaire bilatérale non systématisée, asymétrique, alveole interstitielle", choices=Reponse)
    Epanchement_pleuralRadiologique=forms.ChoiceField(label="Epanchement pleural", choices=Reponse)
    AutreInfoRadiologigue=forms.CharField(label="Autre Information Radiologigue (Preciser)", max_length=9999)
    ##information Biologique
    CRP=forms.IntegerField(label="CRP")
    Pro_calcitonine=forms.IntegerField(label="Pro_calcitonine")
    Albuminémie=forms.IntegerField(label="Albuminémie")
    Ferritine=forms.IntegerField(label="Ferritine")
    Sélenium=forms.IntegerField(label="Sélenium")
    Phosphorémie=forms.IntegerField(label="Phosphorémie")
    Pao2=forms.IntegerField(label="Pa02")
    LDH=forms.IntegerField(label="LDH")
    Tx_de_Globules_blancs=forms.IntegerField(label="Tx_de_Globules_blancs")
    Tx_de_plaquettes=forms.IntegerField(label="Tx_de_plaquettes")
    Tx_de_lymphocytes=forms.IntegerField(label="Tx_de_lymphocytes")
    SGPT=forms.IntegerField(label="SGPT")
    SGOT=forms.IntegerField(label="SGOT")
    Bilirubine=forms.IntegerField(label="Bilirubine")
    Phosphatases_alcalines=forms.IntegerField(label="Phosphatases_alcalines")
    Urée=forms.IntegerField(label="Urée")
    Créatinémie=forms.IntegerField(label="Créatinémie")
    Natrémie=forms.IntegerField(label="Natrémie")
    Kaliémie=forms.IntegerField(label="Kaliémie")
    Proteinurie=forms.IntegerField(label="Proteinurie")
    Hématurie=forms.IntegerField(label="Hématurie")
    CPK=forms.IntegerField(label="CPK")
    #Traitement reçu et prise en charge
    traitementAvantConsultation=forms.CharField(label="A reçu un traitement avant votre consultation :", max_length=8484,required=False)
    traitementEncours=forms.CharField(label="Traitement en cours actuellement :", max_length=8484,widget=forms.Textarea,required=False)
    AutreTraitementimmunosuppresseur=forms.CharField(label="si autre traitement immunosuppresseur que cité précédemment, le préciser :", max_length=8484,widget=forms.Textarea,required=False)
    #quelun sup coordoonners
    InfoSupDunEntourage=forms.CharField(label=" Connaissez-vous une personne ou plus, de votre entourage familial et/ou professionnel et/ou social (amis,..) qui a /ont les mêmes  symptômes que vous ? Si oui, préciser l’identité de cette/ces personnes et leurs coordonnées",widget=forms.Textarea,required=False)
    #Questionnaire adressé avec les prélèvements suivants : (cocher les cases correspondantes uniquement)
    Liquide_de_ponction_pleurale=forms.DateField(label="Liquide de ponction pleurale")
    Crachats=forms.DateField(label="Crachat")
    Liquides_d_aspirations=forms.DateField(label="Liquides d'aspirations")
    Lavage_broncho_pulmonaires=forms.DateField(label="Lavage broncho pulmonaires")
    Urines=forms.DateField(label="Urines")
    Sang=forms.DateField(label="Sang")      
    AutrePrelevement=forms.DateField(label="Autre prelevement")

    
        
        
