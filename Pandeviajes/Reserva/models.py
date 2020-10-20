from django.db import models

# Create your models here.
class Reserva(models.Model):
	nombres=models.CharField(max_length=60)
	apep=models.CharField(max_length=20)
	apem=models.CharField(max_length=20)
	rut=models.CharField(max_length=9)
	edad=models.IntegerField(max_length=9)
	cantP=models.IntegerField(max_length=3)
	telef=models.IntegerField(max_length=9)
	SEL_DEST = (
		('NA', 'Selecciona un destino'),
		('HAWAI', 'Hawai'),
		('PARIS', 'Paris'),
		('MOSCY', 'Moscu'),
		('TOKIO', 'Tokio'),
		('SHANGAI', 'Shangai'),
		('BERLIN', 'Berlin'),
		('DUBAI', 'Dubai'),
	)

	destinos = models.CharField(
		max_length=21,
		choices=SEL_DEST,
		blank=True,
		default='NA',
		help_text='Destinos',
	)
    
	
	def _str_(self):
		return self.nombre	

class Contacto(models.Model):
	nombre = models.CharField(max_length=20)
	apellido = models.CharField(max_length=20)
	mensaje=models.TextField(max_length=2000)
	correo = models.EmailField(default=None)


	def _str_(self):
		return self.nombre