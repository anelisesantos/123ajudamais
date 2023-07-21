"""
URL configuration for projeto_123ajuda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from core import views

urlpatterns = [
    path('', views.PaginaInicialView.as_view(), name='pagina_inicial'),
    path('admin/', admin.site.urls),
    path('cadastro/psicologo/', views.PsicologoCadastroView.as_view(), name='cadastro_psicologo'),
    path('cadastro/paciente/', views.PacienteCadastroView.as_view(), name='cadastro_paciente'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('centros_psicossociais/', views.CentrosPsicossociaisView.as_view(), name='centros_psicossociais'),
]
