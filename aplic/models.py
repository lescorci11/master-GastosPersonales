from django.db import models

class Usuario(models.Model):
    identificacion       = models.CharField(max_length=15)
    nombreUsuario        = models.CharField(max_length=200, blank=True)
    nombres              = models.CharField(max_length=100, blank=True)
    apellidos            = models.CharField(max_length=100, blank=True)
    email                = models.EmailField(max_length=100, blank=True)
    idEstadoUsuario      = models.IntegerField()
    eliminado            = models.BooleanField(default=False)

    def __str__(self):
        return self.nombreUsuario
        
class Ingreso(models.Model):
    idIngreso            = models.CharField(max_length=15)
    fechaIng             = models.DateField()
    descripcionIng       = models.CharField(max_length=100, blank=True)
    valorIng             = models.DecimalField(max_digits=10, decimal_places=2)
    idEstadoIngreso      = models.IntegerField()
    usuario              = models.ForeignKey('Usuario')
    eliminado            = models.BooleanField(default=False)
    
    def __str__(self):
            return self.idIngreso
 
  
class Gasto(models.Model):
    idGasto              = models.CharField(max_length=15)
    fechaGas             = models.DateField()
    descripcionGas       = models.CharField(max_length=100, blank=True)
    valorGas             = models.DecimalField(max_digits=10, decimal_places=2)
    idEstadoGas          = models.IntegerField()
    usuario              = models.ForeignKey('Usuario')
    eliminado            = models.BooleanField(default=False)
    
    def __str__(self):
        return self.idGasto
    

class Parametro(models.Model):
    atributo        =models.CharField(max_length=50)
    descripcion      =models.CharField(max_length=200)
    estadoParametro =models.CharField(max_length=1)
 
    def __str__(self):
        return self.atributo


class ValorParametro(models.Model):
    
    valor                =models.CharField(max_length=30)
    parametro            = models.ForeignKey('Parametro')
    orden                =models.CharField(max_length=3)
    estadoValorParametro =models.CharField(max_length=1)
    

    def __str__(self):
        return self.valor
