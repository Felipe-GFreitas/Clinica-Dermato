from django.shortcuts import render, redirect,get_object_or_404
from app.forms import MedicosForm
from app.models import Medicos
from django.core.paginator import Paginator


def home(request):
    return render(request, 'index.html')

def medicos(request):
    search = request.GET.get('search', '') 
    medicos_list = Medicos.objects.filter(nome__icontains=search) 
    # Configura a paginação
    paginator = Paginator(medicos_list, 10)  
    page_number = request.GET.get('page') 
    page_obj = paginator.get_page(page_number) 
    return render(request, 'Medicos.html', {'db': page_obj, 'search': search})

def create_medicos(request):
    if request.method == 'POST':
        form = MedicosForm(request.POST)
        if form.is_valid():
            form.save()  # Salva os dados se forem válidos
            return redirect('medicos')  # Redireciona para a página de pacientes após salvar
        else:
            # Se o formulário for inválido, renderiza novamente o formulário com erros
            return render(request, 'MedicosForm.html', {'form': form})
    else:
        form = MedicosForm()
    return redirect('formmedicos')

def formMedicos(request):
    data = {}
    data['form'] = MedicosForm() 
    return render(request, 'MedicosForms.html', data)

def delete_medicos(request, pk):
    db = Medicos.objects.get(pk=pk)
    db.delete()
    return redirect('medicos')

def view_medicos(request, pk):
    medico = get_object_or_404(Medicos, pk=pk) 
    return render(request, 'MedicosView.html', {'db': medico})

def edit_medicos(request,pk):
    medicos = get_object_or_404(Medicos, pk=pk)
    form = MedicosForm(instance=medicos)
    return render(request, 'MedicosForms.html', {'form': form, 'db': medicos})

def update_medicos(request,pk):
    medicos = get_object_or_404(Medicos, pk=pk)
    form = MedicosForm(request.POST, instance=medicos)
    if form.is_valid():
        form.save()
        return redirect('medicos')
    return render(request, 'MedicosForms.html', {'form': form, 'db': medicos})