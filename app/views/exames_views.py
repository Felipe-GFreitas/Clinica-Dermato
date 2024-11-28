from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from app.models import Exames
from app.forms import ExameForm

# Lista de exames
def listar_exames(request):
    exames = Exames.objects.all().order_by('-data_solicitacao')
    return render(request, 'exames.html', {'exames': exames})

# Criar exame
def criar_exame(request):
    if request.method == 'POST':
        form = ExameForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exame criado com sucesso!')
            return redirect('listar_exames')
    else:
        form = ExameForm()
    return render(request, 'ExamesCriar.html', {'form': form})

# Editar exame
def editar_exame(request, exame_id):
    exame = get_object_or_404(Exames, id=exame_id)
    if request.method == 'POST':
        form = ExameForm(request.POST, instance=exame)
        if form.is_valid():
            form.save()
            messages.success(request, 'Exame atualizado com sucesso!')
            return redirect('listar_exames')
    else:
        form = ExameForm(instance=exame)
    return render(request, 'ExamesEditar.html', {'form': form, 'exame': exame})

# Excluir exame
def excluir_exame(request, exame_id):
    exame = get_object_or_404(Exames, id=exame_id)
    if request.method == 'POST':
        exame.delete()
        messages.success(request, 'Exame excluído com sucesso!')
        return redirect('listar_exames')
    return render(request, 'ExamesExcluir.html', {'exame': exame})
