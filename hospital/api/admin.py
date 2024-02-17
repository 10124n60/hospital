from django.contrib import admin
from .models import Medic, Spetiality, Service, Patient, Visit

admin.site.register(Medic)
admin.site.register(Spetiality)
admin.site.register(Service)
admin.site.register(Patient)
admin.site.register(Visit)
