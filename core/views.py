from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AbstractUser
from django.utils.decorators import method_decorator
from .forms import PsicologoCadastroForm, PacienteCadastroForm
from .models import CentroPsicossocial

class UserProfile(AbstractUser):
    # Adicione campos extras de perfil, se necessário
    pass

class PaginaInicialView(View):
    def get(self, request):
        return render(request, 'index.html')

class PsicologoCadastroView(View):
    def get(self, request):
        form = PsicologoCadastroForm()
        return render(request, 'cadastro_psicologo.html', {'form': form})

    def post(self, request):
        form = PsicologoCadastroForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            senha = form.cleaned_data['senha']
            # Lógica para processar o cadastro do psicólogo
            return render(request, 'cadastro_sucesso.html')
        return render(request, 'cadastro_psicologo.html', {'form': form})

class PacienteCadastroView(View):
    def get(self, request):
        form = PacienteCadastroForm()
        return render(request, 'cadastro_paciente.html', {'form': form})

    def post(self, request):
        form = PacienteCadastroForm(request.POST)
        if form.is_valid():
            # Lógica para processar o cadastro do paciente
            return render(request, 'cadastro_sucesso.html')
        return render(request, 'cadastro_paciente.html', {'form': form})

class LoginView(View):
    def get(self, request):
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pagina_inicial')
        return render(request, 'login.html', {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('pagina_inicial')

class CentrosPsicossociaisView(View):
    @method_decorator(login_required)
    def get(self, request):
        centros_psicossociais = CentroPsicossocial.objects.all()
        return render(request, 'centros_psicossociais.html', {'centros_psicossociais': centros_psicossociais})
    
# Create your views here.
