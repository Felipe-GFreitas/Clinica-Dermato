from django import forms
from app.models import Pacientes, Medicos,Consultas,Exames
from datetime import time, timedelta, datetime

class PacientesForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),  # Seletor de data
        input_formats=['%Y-%m-%d', '%d/%m/%Y']  # Formatos aceitos
    )

    class Meta:
        model = Pacientes
        fields = ['nome', 'telefone', 'cpf', 'email', 'data_nascimento']


class MedicosForm(forms.ModelForm):
    class Meta:
        model = Medicos
        fields = ['nome', 'crm', 'especialidade', 'horario']  # Retirei a forma de escolha daqui, pq já estou colocando no models

class AgendamentoForm(forms.ModelForm):

    class Meta:
        model = Consultas
        fields = ['paciente', 'medico', 'data_consulta', 'hora_consulta', 'observacoes']
        widgets = {
            'data_consulta': forms.DateInput(attrs={'type': 'date'}),
        }

    hora_consulta = forms.ChoiceField(choices=[], label="Horário da Consulta")

    def __init__(self, *args, **kwargs):
        super(AgendamentoForm, self).__init__(*args, **kwargs)
        self.fields['hora_consulta'].choices = self.gerar_opcoes_horarios()

    def gerar_opcoes_horarios(self):
        horarios = []
        inicio = datetime.strptime('08:00', '%H:%M')
        fim = datetime.strptime('18:00', '%H:%M')

        while inicio < fim:
            proximo = inicio + timedelta(minutes=30)
            horarios.append((inicio.strftime('%H:%M'), f"{inicio.strftime('%H:%M')} - {proximo.strftime('%H:%M')}"))
            inicio = proximo

        return horarios
    
class ExameForm(forms.ModelForm):
    class Meta:
        model = Exames
        fields = ['paciente', 'consulta', 'tipo_exame', 'data_realizacao', 'status', 'resultados']
        widgets = {
            'data_realizacao': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'resultados': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }