from django.shortcuts import render
from aplic.models import Usuario
from django.template import RequestContext
from django.shortcuts import get_object_or404, render_to_response,redirect
from django.contrib.auth import authenticate, login
def index(request):
	if request.user.is_authenticated():
		return render_to_response("aplic/index.html",{},
		context_instance=RequestContext(request))
	else:
		return redirect("/login")

	def usuarios(request):
		usuarios=Usuario.objects.all()
		"""x="<h1>Lista de Usuarios</h1><br>"
		x+="<br>".join(["identificacion: %s, nombreUsuario:%s %s," %(c.identificacion,c.nombreUsuario,c.nombres,c.apellidos) for c in usuarios)])
		return HttpResponse(x)"""
		return render_to_response("aplic/listarUsuarios.html",{'usuarios':usuarios},
			context_instance=RequestContext(request))

def Crear_usuario(request):
	if request.method =="POST":
		form=UsuarioForm(reques.POST)
		if form.is_valid():
			form.save()
			return redirect("/usuarios")
	else:
		form=UsuarioForm()
		return render_to_response("aplic/CrearUsuarios.html",
			                      {'form':form},
			                      context_instance)RequestContext(request))