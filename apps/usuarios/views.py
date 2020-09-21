from django.shortcuts import render
from django.views.generic import CreateView
from apps.usuarios.models import usuarios
from apps.usuarios.forms import RegistroForm,EditForm
from django.urls import reverse_lazy
# Create your views here.



class RegistroUsuario(CreateView):
	model = usuarios
	template_name = "feria/registro.html"
	form_class = RegistroForm
	success_url = reverse_lazy('base:index')


