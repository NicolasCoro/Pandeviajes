from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('reserva/<int:pk', views.ReservaDetailView.as_view(), name='reserva_detail'),
]
urlpatterns+=[
    path('reserva/create/', views.ReservaCreate.as_view(), name= 'reserva_create'),
    path('reserva/<int:pk>/update/' ,views.ReservaUpdate.as_view(), name='reserva_update'),
    path('reserva/<int:pk>/delete/',views.ReservaDelete.as_view(), name='reserva_delete'),

]