from django.shortcuts import render
from . models import Reserva, Contacto
from django.views import generic


# Create your views here. 
def index(request):
    num_reserva= Reserva.objects.all().count()
    num_contacto= Contacto.objects.all().count()

    num_reserva_available=Reserva.objects.filter(destinos__exact='hawai').count()

    return render(
        request,
        'index.html',
        context={'num_reserva': num_reserva,'num_contacto:':num_contacto,
                'num_reserva_available':num_reserva_available},
    )
def Destinos(request):

    return render(
        request,
        'Destinos.html',
    )
def Pasajes(request):

    return render(
        request,
        'Pasajes.html',
    )


    

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class ReservaCreate(CreateView):
    model= Reserva
    fields= '__all__'
    initial={'destinos': 'NA'}
class ReservaUpdate(UpdateView):
    model= Reserva
    fields= '__all__'
class ReservaDelete(DeleteView):
    model = Reserva
    success_url= reverse_lazy(Reserva)   

class ReservaListView(generic.ListView):
    model= Reserva
    paginate_by=10

class ReservaDetailView(generic.DetailView):
    model: Reserva 




