from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
	def _create_user(self, username, email, password, is_staff,is_superuser,**extra_fields):
		if not email:
			raise ValueError('El email debe ser obligatorio')
		email= self.normalize_email(email)
		user = self.model(username=username, email=email, is_active=True,
				is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
		user.set_password(password)
		user.save(using = self._db)
		return user
	def create_user(self, username, email, password=None ,**extra_fields):
		return self._create_user(username, email, password, False,False, **extra_fields)
	def create_superuser(self, username, email, password, **extra_fields):
		return self._create_user(username, email, password, True,True, **extra_fields)

class usuarios(AbstractBaseUser, PermissionsMixin):

	id_user = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
	username = models.CharField('Nombre de usuario',max_length=50, unique = True)
	email = models.EmailField('Correo electronico', max_length=254, unique = True)
	first_name = models.CharField('Primer nombre',max_length=100)
	last_name = models.CharField('Apellido',max_length=100)
	direccion = models.CharField('Direccion', max_length=50)
	objects = UserManager()
	is_active = models.BooleanField('Esta activo',default=True)
	is_staff = models.BooleanField('Es administrador',default=False)
	tipos = (('productor','Productor'),('interno','Interno'),('externo','Externo'),('consultor','Consultor'),('transportista','Transportista'))
	tipo_usuario = models.CharField(max_length=50,choices=tipos,default='consultor')

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def get_short_name(self):
		return self.username

