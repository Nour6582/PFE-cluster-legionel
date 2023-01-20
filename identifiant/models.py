
from ast import mod
from calendar import c
from platform import mac_ver
from re import L
from turtle import back
from unittest import mock
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class TypeUser(models.TextChoices):
    Médecin='Médecin'
    laboratoire_biologique='laboratoire biologique'
    centre_radiologique='centre radiologique'
   

class User(AbstractUser):
   
    
    telPortable=models.IntegerField(('Tel portable'),blank=True,null=True)
    fax=models.IntegerField(blank=True,null=True)
    #nomUser=models.CharField(max_length=30,blank=True,unique=True,null=True)
    #lieu_residence=models.ForeignKey("lieu",blank=True,on_delete=models.SET_NULL,null=True)
    spécialité=models.CharField(max_length=100,blank=True,null=True)
    NumLicenceMedecin=models.CharField(("Numero de licence du medecin si c'est le cas"),max_length=30,blank=True,unique=True,null=True)
    NumLicenceResponsable=models.CharField(("numero  de licence du responsable du laboratoire biologique ou centre de radiologie"),max_length=30,blank=True,unique=True,null=True)
    Num_Autorisation=models.CharField(("numero d'autorisation d'exploitation"),max_length=100,blank=True,unique=True,null=True)
    Nom_laboHopital=models.CharField(("Le nom de l'hopital/laboratoire biologique/centre radiologique"),max_length=100,blank=True,unique=True,null=True)
    typeIntroducteur=models.CharField(("Type du compte"),choices=TypeUser.choices,max_length=30,default=True)
    is_valide=models.BooleanField(default=False)
    Wilaya=models.CharField(max_length=100)
    Daira=models.CharField(max_length=100)
    Commune=models.CharField(max_length=100)
    
    def __str__(self):
        return  f"{self.username}  "

def post_user_created_signal(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal,sender=User)










#creer l user en utilisant le numero de securite pour associer le compte 







class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.user.username


 ############ Identification de la personne qui INTRODUIT le questionnaire ###########

#class radioclinique(models.TextChoices):
    #radiologique='radiologique'#    biologique='biologique'

    ############ Models Pour le laboratoire ########### 
#class laboratoire(models.Model):
   # NomLabo=models.CharField(max_length=100) 
   # typelabo=models.CharField(choices=radioclinique.choices,blank=True,max_length=45) 
    #userprofile=models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    #medecin=models.ForeignKey(User,on_delete=models.CASCADE)
    #def __str__(self):
        #return self.NomLabo




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

  ############ Models Pour Identification du patient###########
class lieu(models.Model):
    wilaya=models.CharField(max_length=100)
    Daira=models.CharField(max_length=100)
    Commune=models.CharField(max_length=100)
    def __str__(self):
        return  f"{self.wilaya} {self.Daira} {self.Commune}"

class adresseResidence(models.Model):
    NumRue=models.IntegerField(("Numero de la Rue"))
    NomRue=models.CharField(("Nom de la Rue"),max_length=100)
    CodePostal=models.IntegerField(("Code Postal"),blank=True)
    NumBoitePostal=models.IntegerField(("Numero de la Boite Postal"),blank=True)
    NumBattiment=models.IntegerField(("Numero du Battiment"))
    NumAppartement=models.IntegerField(("Numero de l'appartement"),blank=True)
    #adressewilaya=models.CharField(max_length=100)
    #adresseDaira=models.CharField(max_length=100)
    #adresseCommune=models.CharField(max_length=100)
    adresse=models.ForeignKey('lieu',on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.NumRue} {self.NomRue} {self.CodePostal}"

class sexe(models.TextChoices):
    masculin='M'
    feminin='F'



######### Cas detectant la maladie legionell
#class SignMaladie(models.Model):
 #   sign1=models.CharField(("Diagnostic de pathologie chronique"),max_length=1000)





class CasMalade(models.TextChoices):
    Confirmé='Confirmé'
    Probale='Probable'
    Negatif='Negatif'



class identitePatient(models.Model):
    #identity=models.OneToOneField("id",on_delete=models.CASCADE)
    Nom=models.CharField(max_length=30)
    NomMarital=models.CharField(max_length=30,blank=True)
    Prenom=models.CharField(blank=True,max_length=30)
    sexe=models.CharField(choices=sexe.choices,blank=True,max_length=8)
    Date_naissance=models.DateField(("Date de naissance"),blank=True)
    lieu_naissance=models.ForeignKey("lieu",blank=True,on_delete=models.SET_NULL,null=True)
    Tel=models.IntegerField()
    fax=models.IntegerField()
    Email=models.EmailField(blank=True)

    casmalade=models.CharField(choices=CasMalade.choices,blank=True,max_length=30)
    
    

    ResidencePermanent=models.ForeignKey("adresseResidence",on_delete=models.CASCADE)
    InfoClinique=models.OneToOneField("InfoClinique",on_delete=models.SET_NULL,null=True,blank=True)
    InfoRadiologique=models.OneToOneField("InfoRadiologique",on_delete=models.SET_NULL,null=True,blank=True)
    InfoBiologique=models.OneToOneField("InfoBiologique",on_delete=models.SET_NULL,null=True,blank=True)
    
    QuestionAvecPrelevement=models.OneToOneField("QuestionAvecPrelevement",on_delete=models.SET_NULL,null=True,blank=True)
    userprofile=models.ForeignKey("UserProfile",on_delete=models.CASCADE)
    
    def __str__(self):
        return  f"{self.Nom} {self.Prenom} {self.casmalade}"
  
 
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

  ############ Models Pour le formulaire###########


class patientvu(models.TextChoices):
    hospitalisation='hospitalisation'
    HDJ='HDJ'
    Consultation='Consultation en dehors de CPU'
    PU='PU'

class etatDuPatient(models.TextChoices):
    Gueri='Guéri'
    Malade='Malade'
    Decede='Décédé'



    
class formulaire(models.Model):
    Date_Introduction=models.DateField()
    patientvu=models.CharField(("Patient Vu"),choices=patientvu.choices,max_length=45)
    ###############identite du patient 
    identitePatient=models.OneToOneField("identitePatient",on_delete=models.CASCADE)

    #iintroducteur de l'information
    medecin=models.ForeignKey(User,on_delete=models.CASCADE)

    etatDuPatient=models.CharField(("Etat du patient"),choices=etatDuPatient.choices,max_length=45)
    DiagnosticDepathologiChronique=models.CharField(("Diagnostic de pathologie chronique"),max_length=1000)
    SipathologieChroniqueAso=models.CharField(("Si Pathologie chronique associée "),blank=True,max_length=4005)
    #facteurRisque
    facteurRisque=models.ForeignKey("facteurRisque",on_delete=models.SET_NULL,null=True)
    #Si Thérapie immunosuppressive en cours, préciser
    Therapieimmunosuppressiveencours=models.ForeignKey("Therapieimmunosuppressiveencours",on_delete=models.SET_NULL,null=True)
    #Informations cliniques des le début de la Maladie c.-à-d. l’infection respiratoire basse (cocher uniquement ce qui vous correspond): 
    ###traitement recu avant
    traitementRecu=models.OneToOneField("traitementRecu",on_delete=models.SET_NULL,null=True,blank=True)
    InfoSupDunEntourage=models.CharField(max_length=995555,blank=True)
    
    #le profile qui est lier a uncompte
    #IntroduitPar = models.ForeignKey(UserProfile,on_delete=models.CASCADE) 
    

####information sur etat du patient au moment de lintroduction du questionnaire

     #facteurRisque
class facteurRisque(models.Model):
    GreffedeMoelleosseuse=models.CharField(max_length=100,blank=True)   
    Greffederein=models.CharField(max_length=100,blank=True) 
    Splenectomie=models.CharField(max_length=100,blank=True) 
    Tabac=models.CharField(max_length=100,blank=True) 



     #Si Thérapie immunosuppressive en cours, préciser
class Therapieimmunosuppressiveencours(models.Model):
    chimiothérapie=models.CharField(max_length=100,blank=True) 
    anti_TNFalpha=models.CharField(max_length=100,blank=True)   
    Corticothérapie=models.CharField(max_length=100,blank=True) 








####information clinique
class Reponse(models.TextChoices):
    
    Je_ne_sais_pas='Je ne sais pas'
    oui='oui'
    

class InfoClinique(models.Model):
    Fievre=models.CharField((" Fièvre à Préciser "),choices=Reponse.choices,max_length=50,default=True)
    Lethargie=models.CharField((" Léthargie"),choices=Reponse.choices,max_length=50,default=True)
    Myalgies_arthralgies=models.CharField((" Myalgies arthralgies"),choices=Reponse.choices,max_length=50,default=True)
    Cephalees=models.CharField((" Céphalées"),choices=Reponse.choices,max_length=50,default=True)
    Tachycardie=models.CharField((" Tachycardie (>ou=100/mn)"),choices=Reponse.choices,max_length=50,default=True)
    Polypnee=models.CharField((" Polypnée (>ou=30/mn)"),choices=Reponse.choices,max_length=50,default=True)
    TouxSeche=models.CharField(("Toux seche"),choices=Reponse.choices,max_length=50,default=True)
    TouxProductive=models.CharField(("Toux productive"),choices=Reponse.choices,max_length=50,default=True)
    TouxPurulente=models.CharField((" Toux purulente"),choices=Reponse.choices,max_length=50,default=True)
    DouleurThoracique=models.CharField(("Douleur Thoracique"),choices=Reponse.choices,max_length=50,default=True)
    Dyspnee=models.CharField((" Dyspnée"),choices=Reponse.choices,max_length=50,default=True)
    DefaillanceRespiratoire=models.CharField((" Défaillance respiratoire"),choices=Reponse.choices,max_length=50,default=True)
    Confusion=models.CharField((" Confusion"),choices=Reponse.choices,max_length=50,default=True)
    Diarrhees=models.CharField(("Diarrhées"),choices=Reponse.choices,max_length=50,default=True)
    Vomissements=models.CharField((" Vomissements"),choices=Reponse.choices,max_length=50,default=True)
    Douleurs_abdominales=models.CharField((" Douleurs abdominales "),choices=Reponse.choices,max_length=50,default=True)
    Epanchement_pleuralClinique=models.CharField((" Epanchement pleural"),choices=Reponse.choices,max_length=50,default=True)
    AutreInfoClinique=models.CharField(max_length=999999999,blank=True)






####information radiologique
class InfoRadiologique(models.Model):
    Opacités_nodulaires_pseudo_tumorales=models.CharField(("Opacités nodulaires pseudo- tumorales"),choices=Reponse.choices,max_length=80,default=True)
    Atteinte_pulmonaire_unilatérale_Droite =models.CharField(("Atteinte pulmonaire unilatérale  Droite"),choices=Reponse.choices,max_length=50,default=True)
    Atteinte_pulmonaire_unilatérale_Gauche   =models.CharField(("Atteinte pulmonaire unilatérale  Gauche"),choices=Reponse.choices,max_length=50,default=True)
    Alvéolaire=models.CharField(("Atteinte pulmonaire bilatérale non systématisée, asymétrique, alvéolaire"),choices=Reponse.choices,max_length=50,default=True)
    alveol_interstitielle =models.CharField(("Atteinte pulmonaire bilatérale non systématisée, asymétrique, alveol interstitielle"),choices=Reponse.choices,max_length=50,default=True)
    Epanchement_pleuralRadiologique=models.CharField(("Epanchement pleural"),choices=Reponse.choices,max_length=50,default=True)
    AutreInfoRadiologigue=models.CharField(("Autre Information Radiologigue (Preciser)"),blank=True,max_length=9999)
           


####information Biologique

class InfoBiologique(models.Model):
    
    CRP=models.IntegerField()
    Pro_calcitonine=models.IntegerField()
    Albuminémie=models.IntegerField() 
    Ferritine=models.IntegerField() 
    Sélenium=models.IntegerField()
    Phosphorémie=models.IntegerField()
    Pao2=models.IntegerField()
    LDH=models.IntegerField()
    Tx_de_Globules_blancs=models.IntegerField(("Tx de Globules blancs"))
    Tx_de_plaquettes =models.IntegerField(("Tx de plaquettes "))
    Tx_de_lymphocytes =models.IntegerField(("Tx de lymphocytes "))
    SGPT=models.IntegerField()
    SGOT=models.IntegerField()
    Bilirubine=models.IntegerField()
    Phosphatases_alcalines =models.IntegerField(("Phosphatases alcalines"))
    Urée=models.IntegerField()
    Créatinémie=models.IntegerField() 
    Natrémie=models.IntegerField()
    Kaliémie=models.IntegerField()
    Proteinurie=models.IntegerField()
    Hématurie=models.IntegerField()
    CPK=models.IntegerField()

class traitementRecu(models.Model):
    traitementEncours=models.CharField(max_length=8484,blank=True)
    traitementAvantConsultation=models.CharField(max_length=8484,blank=True)
    AutreTraitementimmunosuppresseur=models.CharField(max_length=8484,blank=True)

####Question adresse avec prelevement
class QuestionAvecPrelevement(models.Model):
    Liquide_de_ponction_pleurale=models.DateField(('Date de prelevement du Liquide de ponction pleurale'),blank=True)
    Crachats=models.DateField(('Date de prelevement du  Crachats'),blank=True)
    Liquides_d_aspirations=models.DateField(('Date de prelevement du  Liquides d’aspirations'),blank=True)
    Lavage_broncho_pulmonaires=models.DateField(('Date de prelevement du  Lavage broncho-pulmonaires'),blank=True)
    Urines=models.DateField(("Date de prelevement d'urines"),blank=True)
    Sang=models.DateField(('Date de prelevement du  Sang'),blank=True)
    AutrePrelevement=models.CharField(('Autre prelevement '),blank=True,max_length=999999)
