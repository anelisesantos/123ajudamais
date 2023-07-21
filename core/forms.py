from django import forms

class PsicologoCadastroForm(forms.Form):
    nome = forms.CharField(max_length=100, label='Nome')
    email = forms.EmailField(label='Email')
    senha = forms.CharField(widget=forms.PasswordInput, label='Senha')

class PacienteCadastroForm(forms.Form):
    # Definição dos campos do formulário para cadastro de paciente
    nome = forms.CharField(max_length=100, label='Nome')
    email = forms.EmailField(label='Email')
    senha = forms.CharField(max_length=100, widget=forms.PasswordInput(), label='Senha')
