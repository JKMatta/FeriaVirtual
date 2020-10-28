from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.template import RequestContext
from apps.usuarios.models import usuarios
from apps.usuarios.forms import EditForm,EditProfileForm
from apps.sistema.forms import RegistroDeProductos,NuevoContrato,editContrato,RegistroDeTransportes,SolicitarPedido,AprobarPedidos,OfrecerProductos
from apps.sistema.forms import ResponderOferta,OfrecerTransport,ResponderTransporte,SolicitarSeguimiento,EditarSeguimiento
from apps.sistema.models import Productos, Contratos, Pedido,ProcesPedido, Transporte, Seguimiento
from django.contrib.auth.forms import UserChangeForm
# Create your views here.




@login_required	
def index(request):
	return render(request, 'feria/menu.html')




@login_required
def listar_usuarios(request):
	usuario = usuarios.objects.all()
	contexto = {'usuarios':usuario}
	return render(request,'feria/administrador/lista-usuarios.html',contexto)




@login_required
def User_edit(request, id_user):
	usuario = usuarios.objects.get(id_user = id_user)
	contratouser = Contratos.objects.get(usuarios_usuarios_id_user = id_user)
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=usuario)
		form2 = editContrato(request.POST, instance=contratouser)
		if form.is_valid() and form2.is_valid():
			form.save()
			form2.save()
		return redirect('sistema:index')

	else:

		form = EditProfileForm(instance=usuario)
		form2 = editContrato(instance=contratouser)
		args = {'form':form,'form2':form2}
	return render(request, 'feria/administrador/editar-usuarios.html', args)




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
	return render(request, 'feria/productor/registro-productos.html',context )




@login_required
def listar_productos(request):
	producto = Productos.objects.all()
	usuario = usuarios.objects.all()
	contexto = {'productos':producto,'usuarios':usuario}
	return render(request,'feria/lista-productos.html',contexto)




@login_required
def VerContrato(request):
	Usuario = request.user
	contrato = Contratos.objects.filter(usuarios_usuarios_id_user=Usuario.id_user)
	contexto = {'contra': contrato}
	return render(request, 'feria/ver-contrato.html', contexto)




@login_required
def Contrato(request):
	form = NuevoContrato(request.POST, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('sistema:index')
	else:
		form = NuevoContrato()
	context = {
		'form': form,
	}
	return render(request, 'feria/contrato.html',context )




@login_required
def registrartransportes(request):
	form = RegistroDeTransportes(request.POST, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('sistema:index')
	else:
		form = RegistroDeTransportes()
	context = {
		'form': form,
	}
	return render(request, 'feria/transportista/registro-transportes.html',context )




@login_required
def solicitarpedido(request):
	form = SolicitarPedido(request.POST, request.FILES or None)
	if form.is_valid():
		form.save()
		return redirect('sistema:index')
	else:
		form = SolicitarPedido()
	context = {
		'form': form,
	}
	return render(request, 'feria/cliente/solicitar-pedido.html',context )




@login_required
def listar_pedidos(request):
	pedido = Pedido.objects.all()
	contexto = {'pedidos':pedido}
	return render(request,'feria/lista-pedidos.html',contexto)




@login_required
def AdministrarPedido(request, id_ped):
	adminpedido = Pedido.objects.get(id_ped = id_ped)
	if request.method == 'POST':
		form = AprobarPedidos(request.POST, instance=adminpedido)
		if form.is_valid():
			form.save()
		return redirect('sistema:index')
	else:
		form = AprobarPedidos(instance=adminpedido)
		args = {'form':form}
	return render(request, 'feria/administrador/administrar-pedido.html', args)




@login_required
def lista_ofrecer(request):
	pedido = Pedido.objects.all()
	contexto = {'pedidos':pedido}
	return render(request,'feria/productor/lista-ofrecer.html',contexto)




@login_required
def OfertaProducto(request, id_ped):
	ofrecer = Pedido.objects.get(id_ped = id_ped)
	producto = Productos.objects.all()
	if request.method == 'POST':
		form = OfrecerProductos(request.POST, instance=ofrecer)
		if form.is_valid():
			form.save()
		return redirect('sistema:index')
	else:
		form = OfrecerProductos(instance=ofrecer)
		args = {'form':form,'productos':producto}
	return render(request, 'feria/productor/ofrecer-productos.html', args)




@login_required
def lista_procesopedidos(request):
	pedido = Pedido.objects.all()
	contexto = {'pedidos':pedido}
	return render(request,'feria/cliente/lista-mispedidos.html',contexto)




@login_required
def ResponderOfertas(request, id_ped):
	respondofert = Pedido.objects.get(id_ped = id_ped)
	producto = Productos.objects.all()
	if request.method == 'POST':
		form = ResponderOferta(request.POST, instance=respondofert)
		if form.is_valid():
			form.save()
		return redirect('sistema:index')
	else:
		form = ResponderOferta(instance=respondofert)
		args = {'form':form,'productos':producto}
	return render(request, 'feria/cliente/ver-ofertas.html', args)





@login_required
def lista_sin_transporte(request):
	pedido = Pedido.objects.all()
	contexto = {'pedidos':pedido}
	return render(request,'feria/transportista/lista-sintransporte.html',contexto)





@login_required
def OfertarTransporte(request, id_ped):
	PedidoSelec = Pedido.objects.get(id_ped = id_ped)
	form = OfrecerTransport(request.POST, request.FILES)
	transporte = Transporte.objects.all()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
		return redirect('sistema:index')
	else:
		form = OfrecerTransport()
		args = {'form':form,'PedidoSelec':PedidoSelec,'transportes':transporte}
	return render(request, 'feria/transportista/ofertar-transporte.html', args)





@login_required
def lista_en_proceso(request):
	proceso = ProcesPedido.objects.all()
	seguimiento = Seguimiento.objects.all()
	contexto = {'procesos':proceso,'seguimientos':seguimiento}
	return render(request,'feria/cliente/mis-procesos.html',contexto)




@login_required
def ResponderTransportes(request, id_proc_pedido):
	respondtrans = ProcesPedido.objects.get(id_proc_pedido = id_proc_pedido)
	transporte = Transporte.objects.all()
	if request.method == 'POST':
		form = ResponderTransporte(request.POST, instance=respondtrans)
		if form.is_valid():
			form.save()
		return redirect('sistema:index')
	else:
		form = ResponderTransporte(instance=respondtrans)
		args = {'form':form,'transportes':transporte}
	return render(request, 'feria/cliente/administrar-transporte.html', args)




@login_required
def Eliminar_ofert_transport(request, id_proc_pedido):
	eliminartrans = ProcesPedido.objects.get(id_proc_pedido = id_proc_pedido)
	if request.method == 'POST':
		eliminartrans.delete()
		return redirect('sistema:index')
	return render(request, 'feria/cliente/eliminar-ofertatrans.html',{'eliminartrans': eliminartrans})






@login_required
def SolicitarSeguimientos(request, id_proc_pedido):
	solicitarseg = ProcesPedido.objects.get(id_proc_pedido = id_proc_pedido)
	if request.method == 'POST':
		form = SolicitarSeguimiento(request.POST)
		if form.is_valid():
			form.save()
		return redirect('sistema:index')
	else:
		form = SolicitarSeguimiento()
		args = {'form':form,'solicitarseg':solicitarseg}
	return render(request, 'feria/cliente/solicitar-seguimiento.html', args)






@login_required
def lista_en_seguimiento(request):
	seguimiento = Seguimiento.objects.all()
	contexto = {'seguimientos':seguimiento}
	return render(request,'feria/mis-seguimientos.html',contexto)





@login_required
def seguimiento_admin(request):
	seguimiento = Seguimiento.objects.all()
	contexto = {'seguimientos':seguimiento}
	return render(request,'feria/administrador/administrar-seguimiento.html',contexto)





@login_required
def AdministrarSeguimientos(request, id_seguimiento):
	adminissegui = Seguimiento.objects.get(id_seguimiento = id_seguimiento)
	if request.method == 'POST':
		form = EditarSeguimiento(request.POST, instance=adminissegui)
		if form.is_valid():
			form.save()
		return redirect('sistema:index')
	else:
		form = EditarSeguimiento(instance=adminissegui)
		args = {'form':form,'adminissegui':adminissegui}
	return render(request, 'feria/administrador/estados-seguimientos.html', args)

