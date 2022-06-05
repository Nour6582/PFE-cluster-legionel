from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)

admin.site.register(identitePatient)
admin.site.register(introducteurDinfo)
#admin.site.register(telephone)
#3admin.site.register(id)
admin.site.register(lieu)
admin.site.register(adresseResidence)
admin.site.register(UserProfile)
admin.site.register(formulaire)
admin.site.register(facteurRisque)
admin.site.register(Therapieimmunosuppressiveencours)
admin.site.register(InfoClinique)
admin.site.register(InfoRadiologique)
admin.site.register(InfoBiologique)
admin.site.register(traitementRecu)
admin.site.register(QuestionAvecPrelevement)

