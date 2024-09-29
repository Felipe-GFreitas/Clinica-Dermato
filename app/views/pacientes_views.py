from django.shortcuts import render, redirect,get_object_or_404
from app.forms import PacientesForm
from app.models import Pacientes
from django.core.paginator import Paginator

#Essa pasta basicamente serve para enviar os dados do banco para algum canto

def home(request):
    return render(request, 'index.html')

def pacientes(request):
    search = request.GET.get('search', '') 
    pacientes_list = Pacientes.objects.filter(nome__icontains=search) 
    # Configura a paginação
    paginator = Paginator(pacientes_list, 10)  
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number) 
    return render(request, 'Pacientes.html', {'db': page_obj, 'search': search})

def formPacientes(request):
    data = {}
    data['form'] = PacientesForm() 
    return render(request, 'PacientesForms.html', data)

def create_paciente(request):
    if request.method == 'POST':
        form = PacientesForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados se forem válidos
            return redirect('pacientes')  # Redireciona para a página de pacientes após salvar
        else:
            # Se o formulário for inválido, renderiza novamente o formulário com erros
            return render(request, 'PacientesForms.html', {'form': form})
    else:
        form = PacientesForm()
    return redirect('formPacientes')

def view_paciente(request, pk):
    data = {}
    data['db'] = Pacientes.objects.get(pk=pk)
    return render(request, 'PacientesView.html', data)

def edit_paciente(request, pk):
    paciente = get_object_or_404(Pacientes, pk=pk)
    form = PacientesForm(instance=paciente)
    return render(request, 'PacientesForms.html', {'form': form, 'db': paciente})

def update_paciente(request, pk):
    paciente = get_object_or_404(Pacientes, pk=pk)
    form = PacientesForm(request.POST, instance=paciente)
    if form.is_valid():
        form.save()
        return redirect('pacientes')
    return render(request, 'PacientesForms.html', {'form': form, 'db': paciente})
    
def delete_paciente(request, pk):
    db = Pacientes.objects.get(pk=pk)
    db.delete()
    return redirect('pacientes')
