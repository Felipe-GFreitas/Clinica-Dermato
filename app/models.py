from django.db import models

class Pacientes(models.Model):  # Tabela de Pacientes
    nome = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField()

    def __str__(self):
        return f"{self.nome} - {self.cpf}"


class Medicos(models.Model):  # Tabela de Médicos
    HORARIO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('integral', 'Integral'),
    ]

    nome = models.CharField(max_length=50)
    crm = models.CharField(max_length=11, unique=True)
    especialidade = models.CharField(max_length=50)
    horario = models.CharField(max_length=10, choices=HORARIO_CHOICES)

    def __str__(self):
        return f"{self.nome} ({self.especialidade}) - CRM: {self.crm}"


class Consultas(models.Model):
    STATUS_CHOICES = [
        ('agendada', 'Agendada'),
        ('concluida', 'Concluída'),
        ('cancelada', 'Cancelada'),
    ]

    paciente = models.ForeignKey('Pacientes', on_delete=models.CASCADE)
    medico = models.ForeignKey('Medicos', on_delete=models.CASCADE)
    data_consulta = models.DateField()
    hora_consulta = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='agendada')
    observacoes = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('medico', 'data_consulta', 'hora_consulta')

    def __str__(self):
        return f"Consulta: {self.paciente.nome} com {self.medico.nome} em {self.data_consulta} às {self.hora_consulta}"


class Exames(models.Model):  # Tabela de Exames
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('realizado', 'Realizado'),
        ('cancelado', 'Cancelado'),
    ]

    paciente = models.ForeignKey('Pacientes', on_delete=models.CASCADE)  # Relacionado ao paciente
    consulta = models.ForeignKey('Consultas', on_delete=models.CASCADE, blank=True, null=True)  # Opcional, mas útil para rastreamento
    tipo_exame = models.CharField(max_length=100)  # Tipo do exame, ex.: "Biópsia", "Dermatoscopia"
    data_solicitacao = models.DateField(auto_now_add=True)  # Data em que o exame foi solicitado
    data_realizacao = models.DateField(blank=True, null=True)  # Data em que o exame foi realizado
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    resultados = models.TextField(blank=True, null=True)  # Detalhes ou observações dos resultados

    def __str__(self):
        return f"Exame: {self.tipo_exame} - {self.paciente.nome} ({self.status})"
