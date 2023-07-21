from django.contrib.auth.models import AbstractUser
from django.db import models

class CentroPsicossocial(models.Model):
    # Seus campos e relacionamentos existentes

class UserProfile(AbstractUser):
    # Campos adicionais, se necessário
    pass

class Informacao(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    texto = models.TextField()

    def __str__(self):
        return self.titulo


class CentroPsicossocial(models.Model):
    nome = models.CharField(max_length=100)
    abrangencia = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    contatos = models.CharField(max_length=200)
    ramais = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.nome

# Create your models here.
