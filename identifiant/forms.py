from django.contrib.auth.forms import UserCreationForm,UserChangeForm,UsernameField

from django.contrib.auth import get_user_model
from django import forms
from .models import *
from identifiant.models import introducteur

User= get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

class createmodelForm(forms.ModelForm):
    class Meta:
        model=introducteur
        fields=(
            'Prenom', 
            'Nom',
            'Email',
            'telephone',
            'fax',
            'tel',
            'user',
            
        )

choixlieu= ( 
    ('hospitalisation','hospitalisation'),
    ('HDJ','HDJ'),
    ('Consultation','Consultation en dehors de CPU'),
    ('PU','PU'), )

sexe=(
   ('M','M'),
   ('F','F'),
)      

class createform(forms.Form):
    #Date=forms.DateField(label='  Date d’introduction du questionnaire ')
    #patientvu=forms.ChoiceField(label='Patient ( e ) vu ( e )',choices=choixlieu)
    #identite du patient
    #
    ##
    #
    #######
    Nomp=forms.CharField(label='Nom (de jeune fille si femme)',max_length=30)
    Nommaritalp=forms.CharField(label='Nom marital ( si femme) ',max_length=30,required=False)
    Prenomp=forms.CharField(label='Prénom (s) ',max_length=30)
    datenaissance=forms.DateField(label='Date de naissance ')
    Sexe=forms.ChoiceField(choices=sexe)
    Tel=forms.IntegerField(label='Tel (fixe et/ou/portable) ')
    Fax=forms.IntegerField()
    Email=forms.EmailField()
    #lieu de naissance du patient
    Wilaya=forms.CharField() 
    Daira=forms.CharField(widget=forms.Textarea) 
    Commune=forms.CharField() 
    #adresse de residence permanente du patient
    NumRue=forms.IntegerField(label="Numero de la Rue")
    NomRue=forms.CharField(label="Nom de la Rue",max_length=100)
    CodePostal=forms.IntegerField(label="Code Postal")
    NumBoitePostal=forms.IntegerField(label="Numero de la boite  postale ( si c’est la cas) ",required=False)
    NumBattiment=forms.IntegerField(label="Numéro de la maison ou du bâtiment ")
    NumAppartement=forms.IntegerField(label="Numéro de l’appartement, si c’est le cas ",required=False)
    adresseWilaya=forms.CharField(label='Wilaya') 
    adresseDaira=forms.CharField(label='Daira') 
    adresseCommune=forms.CharField(label='Commune') 
   
    
    #telephone=forms.CharField(label='',max_length=10)
    
    #Tel=forms.IntegerField(label="telephone ligne  directe ou le standard avec le numéro de poste")
        
        
class createmodelform1(forms.Form):
    Wilaya=forms.CharField() 
    Daira=forms.CharField() 
    Commune=forms.CharField() 