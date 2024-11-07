from django.shortcuts import render, redirect,get_object_or_404
from django.core.exceptions import ValidationError
from datetime import datetime, timedelta
from app.models import Consultas
from app.forms import AgendamentoForm

def agendar_consulta(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            consulta = form.save(commit=False)

            try:
                validar_horario_medico(consulta.medico, consulta.hora_consulta)
                verificar_conflito_horario(consulta.medico, consulta.data_consulta, consulta.hora_consulta)
            except ValidationError as e:
                form.add_error(None, e.message)  # Adiciona o erro ao formulário
                return render(request, 'Consultas.html', {'form': form})

            consulta.save()
            return redirect('home')
    else:
        form = AgendamentoForm()
    return render(request, 'Consultas.html', {'form': form})


def validar_horario_medico(medico, hora):
    """Valida se o médico está disponível no horário solicitado."""
    horario = medico.horario.lower()
    if horario == 'manha' and not (8 <= hora.hour < 12):
        raise ValidationError('O médico só atende no período da manhã (8h às 12h).')
    elif horario == 'tarde' and not (12 <= hora.hour < 18):
        raise ValidationError('O médico só atende no período da tarde (12h às 18h).')
    elif horario == 'integral' and not (8 <= hora.hour < 18):
        raise ValidationError('O médico só atende em horário integral (8h às 18h).')

def verificar_conflito_horario(medico, data, hora):
    """Verifica se já existe uma consulta na mesma faixa de 30 minutos."""
    hora_fim = (datetime.combine(data, hora) + timedelta(minutes=30)).time()
    conflito = Consultas.objects.filter(
        medico=medico,
        data_consulta=data,
        hora_consulta__range=(hora, hora_fim)
    ).exists()
    if conflito:
        raise ValidationError('Já existe uma consulta marcada para este horário.')

def listar_consultas(request):
    search_query = request.GET.get('search', '')
    if search_query:
        consultas = Consultas.objects.filter(paciente__nome__icontains=search_query)
    else:
        consultas = Consultas.objects.all()
    return render(request, 'ConsultasMarcadas.html', {'consultas': consultas})

# View para alterar o status da consulta
def alterar_status_consulta(request, consulta_id, novo_status):
    consulta = get_object_or_404(Consultas, id=consulta_id)
    consulta.status = novo_status
    consulta.save()
    return redirect('listar_consultas')