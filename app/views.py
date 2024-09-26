from django.shortcuts import render, redirect
from app.forms import PacientesForm
from app.models import Pacientes
from django.core.paginator import Paginator

#Essa pasta basicamente serve para enviar os dados do banco para algum canto

def home(request):
    search = request.GET.get('search', '') 
    pacientes_list = Pacientes.objects.filter(nome__icontains=search) 
    # Configura a paginação
    paginator = Paginator(pacientes_list, 10)  
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number) 
    return render(request, 'index.html', {'db': page_obj, 'search': search})

def formPacientes(request):
    data = {}
    data['form'] = PacientesForm() 
    return render(request, 'Pacientes.html', data)

def create(request):
    if request.method == 'POST':
        form = PacientesForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados se forem válidos
            return redirect('home')  # Redireciona para a página inicial após salvar
        else:
            # Se o formulário for inválido, renderiza novamente o formulário com erros
            return render(request, 'Pacientes.html', {'form': form})
    else:
        form = PacientesForm()
    return redirect('formPacientes')  # Redireciona para o formulário caso a solicitação não seja POST

#Todas as coisas da view
def view(request, pk):
    data = {}
    data['db'] = Pacientes.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Pacientes.objects.get(pk=pk)
    data['form'] =PacientesForm(instance= data ['db'])
    return render(request, 'Pacientes.html', data)

def update(request, pk):
    data = {}
    data['db'] = Pacientes.objects.get(pk=pk)
    form = PacientesForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')
    
def delete(request, pk):
    db = Pacientes.objects.get(pk=pk)
    db.delete()
    return redirect('home')

