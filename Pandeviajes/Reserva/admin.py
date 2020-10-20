from django.contrib import admin

# Register your models here.
from . models import Reserva, Contacto

admin.site.register(Reserva)
admin.site.register(Contacto)