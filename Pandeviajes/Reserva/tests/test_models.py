from django.test import TestCase
from . models import Reserva, Contacto

class ReservaTestCase(TestCase):
    def setUp(self):
        a1=Reserva.objects.create(rut="206270578")
        a2=Reserva.objects.create(rut="123456789")
        Contacto.objects.create(correo="asd@123.com", Reserva=a1)
        Contacto.objects.create(correo="nico@hotmail.com", Reserva=a2)
    
    def test(self):
        Contacto1= Contacto.objects.get(rut="asd@123.com")
        self.assertEqual(Contacto1.Reserva.rut,"206270578")

