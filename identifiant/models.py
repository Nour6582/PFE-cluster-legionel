
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class patientvu(models.TextChoices):
    hospitalisation='hospitalisation'
    HDJ='HDJ'
    Consultation='Consultation en dehors de CPU'
    PU='PU'

class localisation(models.Model):
    patientvu=models.CharField(("Patient Vu"),choices=patientvu.choices,max_length=45)
    Date_Introduction=models.DateField()

class User(AbstractUser):
    #tel=models.IntegerField()
    is_introducteur=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username
        
class introducteur(models.Model):
    tel=models.IntegerField(("telephone ligne  directe ou le standard avec le numéro de poste"))
    #identity=models.OneToOneField(id,on_delete=models.CASCADE)
    Nom=models.CharField(max_length=30)
    Prenom=models.CharField(primary_key=True,blank=True,max_length=30)
    Email=models.EmailField(blank=True)
    telephone=models.CharField(max_length=10)
    fax=models.CharField(max_length=10)
    #CHOICES = [('option1','label 1'), ('option2','label 2')] 
    #some_field = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect())
    user=models.OneToOneField(User,on_delete=models.CASCADE)  
    def __str__(self):
        return self.Prenom


class lieu(models.Model):
    wilaya=models.CharField(max_length=100)
    Daira=models.CharField(max_length=100)
    Commune=models.CharField(max_length=100)
    

class adresseResidence(models.Model):
    NumRue=models.IntegerField(("Numero de la Rue"))
    NomRue=models.CharField(("Nom de la Rue"),max_length=100)
    CodePostal=models.IntegerField(("Code Postal"))
    NumBoitePostal=models.IntegerField(("Numero de la Boite Postal"))
    NumBattiment=models.IntegerField(("Numero du Battiment"))
    NumAppartement=models.IntegerField(("Numero de l'appartement"))
    adressewilaya=models.CharField(max_length=100)
    adresseDaira=models.CharField(max_length=100)
    adresseCommune=models.CharField(max_length=100)

class sexe(models.TextChoices):
    masculin='M'
    feminin='F'

class identitePatient(models.Model):
    #identity=models.OneToOneField("id",on_delete=models.CASCADE)
    Nom=models.CharField(max_length=30)
    NomMarital=models.CharField(max_length=30,blank=True)
    Prenom=models.CharField(primary_key=True,blank=True,max_length=30)
    sexe=models.CharField(choices=sexe.choices,blank=True,max_length=8)
    Date_naissance=models.DateField(("Date de naissance"),blank=True)
    lieu_naissance=models.ForeignKey("lieu",blank=True,on_delete=models.SET_NULL,null=True)
    Tel=models.IntegerField()
    fax=models.IntegerField()
    Email=models.EmailField(blank=True)
    ResidencePermanent=models.ForeignKey("adresseResidence",on_delete=models.SET_NULL,null=True)





##
#
##
#
##
#
##
#
#
#
#
#
#
#
#class patientvu(models.TextChoices):
 #   hospitalisation='hospitalisation'
  #  HDJ='HDJ'
 #   Consultation='Consultation en dehors de CPU'
  #  PU='PU'

class etatDuPatient(models.TextChoices):
    Gueri='Guéri'
    Malade='Malade'
    Decede='Décédé'

class formulaire(models.Model):
    Date_Introduction=models.DateField()
    patientvu=models.CharField(("Patient Vu"),choices=patientvu.choices,max_length=45)
    patient=models.BooleanField()
    intro=models.BooleanField()
    etatDuPatient=models.CharField(("Etat du patient"),choices=etatDuPatient.choices,max_length=45)
    DiagnosticDepathologiChronique=models.CharField(("Diagnostic de pathologie chronique"),max_length=1000)
    SipathologieChroniqueAso=models.CharField(("Si Pathologie chronique associée "),blank=True,max_length=4005)
    #Informations cliniques des le début de la Maladie c.-à-d. l’infection respiratoire basse (cocher uniquement ce qui vous correspond): 
