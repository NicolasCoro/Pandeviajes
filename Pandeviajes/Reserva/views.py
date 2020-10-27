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

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ReservaCreate(CreateView):
    model= Reserva
    fields= all
    initial={'destinos': 'NA'}
class ReservaUpdate(UpdateView):
    model= Reserva
    fields= all
class ReservaDelete(DeleteView):
    model = Reserva
    success_url= reverse_lazy(Reserva)   

class ReservaListView(generic.ReservaListView):
    model= Reserva
    paginate_by=10

class ReservaDetailView(generic.DetailView):
    model: Reserva 




