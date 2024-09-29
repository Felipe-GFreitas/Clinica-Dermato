from django.db import models

class Pacientes(models.Model):  # Tabela de pacientes
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=30)
    cpf = models.CharField(max_length=11)  
    email = models.EmailField(max_length=100)  
    data_nascimento = models.DateField()

class Medicos(models.Model):  # Tabela de Medicos
    nome = models.CharField(max_length=30)
    crm = models.CharField(max_length=11) 
    especialidade = models.CharField(max_length=30)  
    horario = models.CharField(max_length=30)  
