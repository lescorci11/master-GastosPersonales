from django.db import models

class Usuario(models.Model):
	identificacion       = models.CharField(max_length=15)
	nombreUsuario        = models.CharField(max_length=50, blank=True)
	nombres              = models.CharField(max_length=100, blank=True)
	apellidos            = models.CharField(max_length=100, blank=True)
	email                = models.EmailField(max_length=100, blank=True)
	eliminado            = models.BooleanField(default=False)

	def __str__(self):
		return self.nombreUsuario

class Ingreso(models.Model):
	idIngreso            = models.CharField(max_length=15)
	fecha                = models.DateField()
	eliminado            = models.BooleanField(default=False)

	def __str__(self):
		return self.idIngreso

class DetalleIngreso(models.Model):
	valorIngreso         = models.DecimalField(max_digits=10, decimal_places=2)
	descripcionIngreso          = models.CharField(max_length=200, blank=True)
	idEstadoDetIngreso   = models.IntegerField()
	eliminado            = models.BooleanField(default=False)

class Gasto(models.Model):
	idGasto            = models.CharField(max_length=15)
	fecha              = models.DateField()
	eliminado          = models.BooleanField(default=False)

	def __str__(self):
		return self.idGasto

class DetalleGasto(models.Model):
	valorGasto          = models.DecimalField(max_digits=10, decimal_places=2)
	descripcionGasto    = models.CharField(max_length=200, blank=True)
	idEstadoDetGasto    = models.IntegerField()
	eliminado           = models.BooleanField(default=False)

class Parametro(models.Model):
	atributo            = models.CharField(max_length=50)
	descripcion         = models.CharField(max_length=200)
	estadoParametro     = models.CharField(max_length=1)

	def __str__(self):
		return self.atributo

class ValorParametro(models.Model):
	valor               = models.CharField(max_length=30)
	orden               = models.CharField(max_length=3)
	estadoValorParametro= models.CharField(max_length=1)

	def __str__(self):
		return self.valor