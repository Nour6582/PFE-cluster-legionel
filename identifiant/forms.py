from argparse import ArgumentError
from email.policy import default
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,UsernameField

from django.contrib.auth import get_user_model
from django import forms
from .models import *


User= get_user_model()



#####updater le use
class updateUsermodelForm(forms.ModelForm):
    class Meta:
        model=User
        fields=(
             'username',
        )

########for registration
class SignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username',
         'email',
          'first_name',
           'last_name', 
           'spécialité',
           'telPortable',
           'fax',
           'typeIntroducteur',
           'Wilaya','Daira','Commune', 
           'NumLicenceMedecin',
    'NumLicenceResponsable',
    'Num_Autorisation',
    'Nom_laboHopital',
    )

###########Chercher un patient pour 


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
    Date_Introduction=forms.DateField(label='  Date d’introduction du questionnaire ',widget=forms.SelectDateWidget(years=(range(2022, 1900, -1))))
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
    datenaissance=forms.DateField(label='Date de naissance ',widget=forms.SelectDateWidget(years=(range(2022, 1900, -1))))
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
    CodePostal=forms.IntegerField(label="Code Postal",required=False)
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
    ####
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
   

   
    
    #Traitement reçu et prise en charge
    traitementAvantConsultation=forms.CharField(label="A reçu un traitement avant votre consultation :", max_length=8484,required=False)
    traitementEncours=forms.CharField(label="Traitement en cours actuellement :", max_length=8484,widget=forms.Textarea,required=False)
    AutreTraitementimmunosuppresseur=forms.CharField(label="si autre traitement immunosuppresseur que cité précédemment, le préciser :", max_length=8484,widget=forms.Textarea,required=False)
    #quelun sup coordoonners
    InfoSupDunEntourage=forms.CharField(label=" Connaissez-vous une personne ou plus, de votre entourage familial et/ou professionnel et/ou social (amis,..) qui a /ont les mêmes  symptômes que vous ? Si oui, préciser l’identité de cette/ces personnes et leurs coordonnées",widget=forms.Textarea,required=False)
    #############sign up d'un compte ########
    #Cas confirmé : au moins un des signes

   
        
    