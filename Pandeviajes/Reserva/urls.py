from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('Destinos/', views.Destinos, name='Destinos'),
    path('Pasajes/', views.Pasajes, name='Pasajes'),
    
    
    path('Rese/<int:pk>', views.ReservaDetailView.as_view(), name='reserva_detail'),

    path('Rese/', views.ReservaListView.as_view(), name='Reserva_list')
]
urlpatterns+=[
    path('Rese/create/', views.ReservaCreate.as_view(), name= 'reserva_create'),
    path('Rese/<int:pk>/update/' ,views.ReservaUpdate.as_view(), name='reserva_update'),
    path('Rese/<int:pk>/delete/',views.ReservaDelete.as_view(), name='reserva_delete'),

]