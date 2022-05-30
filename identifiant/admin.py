from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(User)
admin.site.register(localisation)
admin.site.register(identitePatient)
admin.site.register(introducteur)
#admin.site.register(telephone)
#3admin.site.register(id)
admin.site.register(lieu)
admin.site.register(adresseResidence)
admin.site.register(UserProfile)