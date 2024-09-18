from django.db import models

# Create your models here.

class Pacientes(models.Model):
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)  
    email = models.EmailField(max_length=100)  
    data_nascimento = models.DateField()
    

