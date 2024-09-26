from django import forms
from app.models import Pacientes

#Essa pasta serve para facilitar a criação de formularios

class PacientesForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),  # Campo com seletor de data
        input_formats=['%Y-%m-%d', '%d/%m/%Y']  # Adiciona formatos aceitos
    )

    class Meta:
        model = Pacientes
        fields = ['nome', 'telefone', 'cpf', 'email', 'data_nascimento']
