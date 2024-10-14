# Importações das views de Pacientes
from .pacientes_views import (
    home,
    pacientes,
    formPacientes,
    create_paciente,
    edit_paciente,
    update_paciente,
    delete_paciente,
    view_paciente,
)

# Importações das views de Médicos
from .medicos_views import (
    medicos,
    create_medicos,
    formMedicos,
    delete_medicos,
    view_medicos,
    edit_medicos,
    update_medicos,
)

# Importações das views de Consultas
from .consultas_views import (
    agendar_consulta,
    validar_horario_medico,
    verificar_conflito_horario,
)
