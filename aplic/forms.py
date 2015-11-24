from django import forms
from django.forms import ModelForm
from aplic.models import *

class ParametroForm(forms.Form):
    pass

class UsuarioForm(ModelForm): 
   class Meta:
        model=Usuario
        exclude=["eliminado"]
        

class IngresoForm(ModelForm):
	class Meta:
		model=Ingreso
		exclude=['eliminado']


class GastoForm(ModelForm):
	class Meta:
		model=Gasto
		exclude=['eliminado']