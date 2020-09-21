"""verduras URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from apps.usuarios.views import RegistroUsuario
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib.auth import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include ('apps.base.urls'), name='base'),
    url(r'^registrarse$', RegistroUsuario.as_view(), name='registrarse'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='feria/login.html'), name='login'),
    url(r'^principal/', include ('apps.sistema.urls'), name='base'),
    #url(r'^logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)