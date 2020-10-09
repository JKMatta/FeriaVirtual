from apps.usuarios.models import usuarios
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistroForm(UserCreationForm):

	class Meta:
		model = usuarios

		fields = {
		'username',
		'first_name',
		'last_name',
		'email',
		}
		labels = {
		'username': 'Nombre de usuario',
		'first_name': 'Nombre',
		'last_name': 'Apellido',
		'email': 'Correo',
		}


class EditForm(UserCreationForm):

	class Meta:
		model = usuarios

		fields = {
		'username',
		'password',
		'email',
		'first_name',
		'last_name',
		'direccion',
		'is_active',
		'is_staff',
		'tipo_usuario',
		'is_superuser',
		}
		labels = {
		'username': 'Nombre de usuario',
		'password':'password',
		'email': 'Correo',
		'first_name': 'Nombre',
		'last_name': 'Apellido',
		'direccion': 'Direccion',
		'is_active': 'is_active',
		'is_staff': 'is_staff',
		'tipo_usuario':'Tipo de usuario',
		'is_superuser' : 'is_superuser',
		}


class EditProfileForm(UserChangeForm):

	class Meta:
		model = usuarios

		fields = {
		'email',
		'username',
		'first_name',
		'last_name',
		'is_active',
		'tipo_usuario',
		}

		exclude = {
		'password',
		}