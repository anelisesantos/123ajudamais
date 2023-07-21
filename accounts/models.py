from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Psicologo(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    especializacao = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.usuario.username

class Paciente(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    genero_choices = [
        ('masculino', 'Masculino'),
        ('feminino', 'Feminino'),
        ('outro', 'Outro'),
    ]
    genero = models.CharField(max_length=20, choices=genero_choices)

    def __str__(self):
        return self.usuario.username



# Create your models here.
