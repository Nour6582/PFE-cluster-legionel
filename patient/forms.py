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
    #########update la localisation du patient
    #######update le lieu

#class InfoBiologiqueForm(forms.ModelForm):
   # class Meta:
    #    model=InfoBiologique
     #   fields=(

      #  )
            #############Saving definir le cluster
            
            
            
cas1 =(
        ('Isolement de la souche de Legionella dans des sécretions respiratoires ou dans le tissu pulmonaire ou un epanchement pleural ou tout autre prélèvement qui est normalement stérile.','Isolement de la souche de Legionella dans des sécretions respiratoires ou dans le tissu pulmonaire ou un epanchement pleural ou tout autre prélèvement qui est normalement stérile.'),
        ('Présence d’antigènes urinaires de Legionella pneumophila. Le CDC précise le serogroupe 1 de Legionella pneumophila par des réactifs validés.','Présence d’antigènes urinaires de Legionella pneumophila. Le CDC précise le serogroupe 1 de Legionella pneumophila par des réactifs validés.'),
        ('Sérocoversion : augmentation siginificative d’au moins quatre fois du titre d’anticorps spécifique anti-Legionella pneumophila serogroupe 1 en utilisant des réactifs validés et utilisés sur une paire de sérum prélevés séparemment de trois à six semaines d’intervalle.','Sérocoversion : augmentation siginificative d’au moins quatre fois du titre d’anticorps spécifique anti-Legionella pneumophila serogroupe 1 en utilisant des réactifs validés et utilisés sur une paire de sérum prélevés séparemment de trois à six semaines d’intervalle.'),
        #(forms.CharField(label='Daira'),forms.CharField(label='Daira')),
      
)

cas2=(
    ('Présence d’acides nucléiques (DNA) de Legionella spp dans les sécretions repsiratoires, dans le tissu de poumon ou de toute localisation qui est normalement stérile, par une technique validée (ex : polymerase chain reaction dite PCR).','Présence d’acides nucléiques (DNA) de Legionella spp dans les sécretions repsiratoires, dans le tissu de poumon ou de toute localisation qui est normalement stérile, par une technique validée (ex : polymerase chain reaction dite PCR).'),
    ('Présence d’antigènes de Legionella pneumophila dans les sécrétions respiratoires ou dans le tissu de poumon ou dans l’epanchement pleural ex : immunofluorescence directe en utilisant des anticorps monoclonaux, coloration par immunohistochimie.','Présence d’antigènes de Legionella pneumophila dans les sécrétions respiratoires ou dans le tissu de poumon ou dans l’epanchement pleural ex : immunofluorescence directe en utilisant des anticorps monoclonaux, coloration par immunohistochimie.'),
    ('Séroconversion : augmentation significative d’au moins quatre fois du titre d’anticorps anti-Legionella pneumophila autre que ceux dirigés contre Legionella pneumophila serogroupe 1 ou dirigé contre Legionella spp dans une paire de sérum prélevés séparement de trois à six semaines d’intervalle, en utilisant des réactifs validés.','Séroconversion : augmentation significative d’au moins quatre fois du titre d’anticorps anti-Legionella pneumophila autre que ceux dirigés contre Legionella pneumophila serogroupe 1 ou dirigé contre Legionella spp dans une paire de sérum prélevés séparement de trois à six semaines d’intervalle, en utilisant des réactifs validés.'),
    ('Unique taux élevé d’anticorps spécifique anti-Legionella pneumophila serogroupe 1 dans le sérum. Ceci n’est pas indiqué par le CDC aux états unis.','Unique taux élevé d’anticorps spécifique anti-Legionella pneumophila serogroupe 1 dans le sérum. Ceci n’est pas indiqué par le CDC aux états unis.'),
)




class casMaladeForm(forms.Form):
    casconfirme=forms.MultipleChoiceField(label="Cas confirmé : au moins un des signes",choices=cas1,widget=forms.CheckboxSelectMultiple,required=False)
    casprobable=forms.MultipleChoiceField(label=" Cas probable : au moins un des signes.",choices=cas2,widget=forms.CheckboxSelectMultiple,required=False)


######## Chercher un patient pour les compte du centre biologique et radiologique
class searchForm(forms.Form):
    Nom=forms.CharField(label='Nom (de jeune fille si femme)',max_length=30)
    NomMarital=forms.CharField(label='Nom marital ( si femme) ',max_length=30,required=False)
    Prenom=forms.CharField(label='Prénom (s) ',max_length=30)

