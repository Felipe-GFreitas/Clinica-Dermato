from django.contrib import admin
from django.urls import path
from app.views import (
    home, pacientes, formPacientes, create_paciente, edit_paciente, 
    update_paciente, delete_paciente, view_paciente,
    medicos, formMedicos, create_medicos, delete_medicos, 
    view_medicos, edit_medicos, update_medicos,
    agendar_consulta,listar_consultas,alterar_status_consulta,
    listar_exames,criar_exame,editar_exame,excluir_exame,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    #Urls de tudo que se refere a att de pacientes abaixo
    path('pacientes/', pacientes, name='pacientes'),
    path('pacientes/cadastrar/', formPacientes, name='formPacientes'),
    path('pacientes/create/', create_paciente, name='create_paciente'),
    path('pacientes/view/<int:pk>/', view_paciente, name='view_paciente'),
    path('pacientes/edit/<int:pk>/', edit_paciente, name='edit_paciente'),
    path('pacientes/update/<int:pk>/', update_paciente, name='update_paciente'),
    path('pacientes/delete/<int:pk>/', delete_paciente, name='delete_paciente'),
    #Urls de tudo que se refere a att de medicas abaixo
    path('medicos/', medicos, name='medicos'),
    path('medicos/cadastrar/', formMedicos, name='formMedicos'),
    path('medicos/create/', create_medicos, name='create_medicos'),
    path('medicos/view/<int:pk>/', view_medicos, name='view'),
    path('medicos/edit/<int:pk>/', edit_medicos, name='edit'),
    path('medicos/update/<int:pk>/', update_medicos, name='update'),
    path('medicos/delete/<int:pk>/', delete_medicos, name='delete_medicos'),

    path('agendar-consulta/', agendar_consulta, name='agendar_consulta'),
    path('consultas/', listar_consultas, name='listar_consultas'),
    path('consultas/alterar_status/<int:consulta_id>/<str:novo_status>/', alterar_status_consulta, name='alterar_status_consulta'),

    # URLs de exames
    path('exames/', listar_exames, name='listar_exames'),  # Listar exames
    path('exames/cadastrar/', criar_exame, name='criar_exame'),  # Criar exame
    path('exames/edit/<int:exame_id>/', editar_exame, name='editar_exame'),  # Editar exame
    path('exames/excluir/<int:exame_id>/', excluir_exame, name='excluir_exame'),  # Excluir exame  #
    
]
