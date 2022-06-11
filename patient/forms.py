from django import forms
from identifiant.models import identitePatient,InfoRadiologique,QuestionAvecPrelevement,InfoClinique,InfoBiologique

class updatePatientmodelForm(forms.ModelForm):
    class Meta:
        model=identitePatient
        fields=(
             'Nom',
            'NomMarital',
            'Prenom',
            'sexe',
            'Date_naissance',
        'lieu_naissance',
        'Tel',
    'fax',
    'Email',
    'ResidencePermanent',
        )

class createMailform(forms.Form):
    mail=forms.EmailField(widget=forms.EmailInput)

class InfoRadiologiqueForm(forms.ModelForm):
    class Meta:
        model=InfoRadiologique
        fields=(   
    
    'Opacités_nodulaires_pseudo_tumorales',
   'Atteinte_pulmonaire_unilatérale_Droite' ,
    
    
    'Atteinte_pulmonaire_unilatérale_Gauche',  
    'Alvéolaire',
    'alveol_interstitielle' ,
    'Epanchement_pleuralRadiologique',
    'AutreInfoRadiologigue',
           
        )   
class QuestionAvecPrelevementForm(forms.ModelForm):
    class Meta:
        model=QuestionAvecPrelevement
        fields=(   
    'Liquide_de_ponction_pleurale',
    'Crachats',
    'Liquides_d_aspirations',
    'Lavage_broncho_pulmonaires',
    'Urines',
    'Sang',
    'AutrePrelevement',)  


class InfoCliniqueForm(forms.ModelForm):
    class Meta:
        model=InfoClinique
        fields=(   
                'Fievre',
    'Lethargie',
    'Myalgies_arthralgies',
    'Cephalees',
    'Tachycardie',
      'Polypnee',
    'TouxSeche',
    'TouxProductive',
    'TouxPurulente',
      'DouleurThoracique',
    'Dyspnee',
     'DefaillanceRespiratoire',
      'Confusion',
     'Diarrhees',
    'Vomissements',
    'Douleurs_abdominales',
    'Epanchement_pleuralClinique',
    'AutreInfoClinique',
    )  



    
   
class InfoBiologiqueForm(forms.ModelForm):
    class Meta:
        model=InfoBiologique
        fields=(   
                'CRP',
    'Pro_calcitonine',
    'Albuminémie',
    'Ferritine',
    'Sélenium',
    'Phosphorémie',
    'Pao2',
    'LDH',
    'Tx_de_Globules_blancs',
    'Tx_de_plaquettes',
    'Tx_de_lymphocytes', 
    'SGPT',
    'SGOT',
    'Bilirubine',
    'Phosphatases_alcalines', 
    'Urée',
    'Créatinémie', 
    'Natrémie',
    'Kaliémie',
    'Proteinurie',
    'Hématurie',
    'CPK',
    )  