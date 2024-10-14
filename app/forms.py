from django import forms
from app.models import Pacientes, Medicos,Consultas

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
            'hora_consulta': forms.TimeInput(attrs={'type': 'time'}),
        }
