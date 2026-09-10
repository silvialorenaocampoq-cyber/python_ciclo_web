"""
URL configuration for pr_practica1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.http import HttpResponse
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 1. Mensaje de bienvenida devuelto DIRECTAMENTE desde urls.py
    path('', lambda request: HttpResponse("<h1>¡Bienvenido a la página principal de pr_practica1!</h1>")),
    
    # 2. Mensaje de ayuda desde una función en views.py
    path('ayuda/', views.funcion_ayuda),
    
    # 3. Lista de productos desde la plantilla productos.html
    path('productos/', views.funcion_productos),
]