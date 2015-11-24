from django.http import HttpResponse,HttpResponseRedirect
from aplic.models import *
from aplic.forms import UsuarioForm
from aplic.forms import IngresoForm
from aplic.forms import GastoForm
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response,redirect
from django.contrib.auth import authenticate, login
def index(request):
	if request.user.is_authenticated():
	    return render_to_response("aplic/index.html",{},
	    context_instance=RequestContext(request))  
	else: 
	   return redirect("/login")


def usuarios(request):
	usuarios=Usuario.objects.all()
	"""x="<h1>Lista de Usuarios </h1><br>"
	x+="<br>".join(["id:%s,nombreUsuario: %s,Email:%s %s," %(c.id,c.nombreUsuario,c.nombres,c.apellidos) for c in usuarios ])
	return HttpResponse(x)"""
	return render_to_response("aplic/listarClientes.html",{'usuarios':usuarios},
		context_instance=RequestContext(request))

def ingresos(request):
	ingresos=Ingreso.objects.all()
	"""x="<h1>Lista de Ingresos </h1><br>"
	x+="<br>".join(["id:%s,descripcionIng: %s,valorIng:%s %s," %(c.id,c.descripcionIng, c.fechaIng, c.valorIng,) for c in ingresos ])
	return HttpResponse(x)"""
	return render_to_response("aplic/listarIngreso.html",{'ingresos':ingresos},
		context_instance=RequestContext(request))


def gastos(request):
	gastos=Gasto.objects.all()
	"""x="<h1>Lista de Gastos </h1><br>"
	x+="<br>".join(["id:%s,descripcionGas: %s,valorGas:%s %s," %(c.id,c.descripcionGas, c.fechaGas, c.valorGas) for c in gastos ])
	return HttpResponse(x)"""
	return render_to_response("aplic/listarGasto.html",{'gastos':gastos},
		context_instance=RequestContext(request))

def Crear_gasto(request):
	if request.method =="POST":
		form=GastoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/gastos")
	else:
		form=UsuarioForm()
		return  render_to_response("aplic/CrearGasto.html",
							  	  {'form':form},
							  	  context_instance=RequestContext(request))

def Crear_ingreso(request):
	if request.method =="POST":
		form=IngresoForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/ingresos")
	else:
		form=UsuarioForm()
		return  render_to_response("aplic/CrearIngreso.html",
							  	  {'form':form},
							  	  context_instance=RequestContext(request))

def prueba(request,id):
    x="<h1>"+id+"</h1>"
	#return render_to_response("login",{})
    return HttpResponse(x)


def Crear_usuario(request):
	if request.method =="POST":
		form=UsuarioForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect("/usuarios")
	else:
		form=UsuarioForm()
		return  render_to_response("aplic/CrearClientes.html",
							  	  {'form':form},
							  	  context_instance=RequestContext(request))


def Crear_parametro(request):
	if request.method =="POST":
		form=ParametroForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/parametro")
	else:
		form=ParametroForm()
		return  render_to_response("aplic/CrearParametro.html",
							  	  {'form':form},
							  	  context_instance=RequestContext(request))
		