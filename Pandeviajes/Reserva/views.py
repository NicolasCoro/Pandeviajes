from django.shortcuts import render
from . models import Contacto, Reserva
from django.views import generic

# Create your views here.
def index(request):
    num_reserva= Reserva.objects.all().count()
    num_contacto= Contacto.objects.all().count()

    num_reserva_available=Reserva.objects.filter(destinos__exact='hawai').count()

    return render(
        request,
        'index.html',
        context={'Numero de reservas': num_reserva,'Numero de personas contacto:':num_contacto,
                'Numero de reservas con destino=Hawai':num_reserva_available},
    )


