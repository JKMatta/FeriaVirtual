from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.template import RequestContext
from apps.usuarios.models import usuarios
from apps.usuarios.forms import EditForm,EditProfileForm
from apps.sistema.forms import RegistroDeProductos
from apps.sistema.models import Productos
from django.contrib.auth.forms import UserChangeForm
# Create your views here.


@login_required	
def index(request):
	return render(request, 'feria/menu.html')


@login_required
def listar_usuarios(request):
	usuario = usuarios.objects.all()
	contexto = {'usuarios':usuario}
	return render(request,'feria/lista-usuarios.html',contexto)


@login_required
def User_edit(request, id_user):
	usuario = usuarios.objects.get(id_user = id_user)
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=usuario)

		if form.is_valid():
			form.save()
			return redirect('sistema:index')

	else:

		form = EditProfileForm(instance=usuario)
		args = {'form':form}
		return render(request, 'feria/editar-usuarios.html', args)



@login_required
def registrarproductos(request):
	form = RegistroDeProductos(request.POST, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('sistema:index')
	else:
		form = RegistroDeProductos()
	context = {
		'form': form,
	}
	return render(request, 'feria/registro-productos.html',context )


@login_required
def listar_productos(request):
	producto = Productos.objects.all()
	usuario = usuarios.objects.all()
	contexto = {'productos':producto,'usuarios':usuario}
	return render(request,'feria/lista-productos.html',contexto)

