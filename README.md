Sistema de Consultas e Agendamento para Clínica de Dermatologia
Descrição

Este projeto é um sistema de consultas e agendamento para uma clínica de dermatologia. A aplicação permitirá o gerenciamento de consultas, cadastro de pacientes e médicos, e outras funcionalidades relacionadas ao agendamento de consultas.
Integrantes

    Felipe Gomes de Freitas
    Felipe Martins Menino
    Guilherme Satoru Oku

Tecnologias Utilizadas

    Backend: Django (Python)
    Frontend: HTML, CSS, JavaScript (Bootstrap)
    Banco de Dados: MySQL
    Ferramentas de Desenvolvimento: MySQL Workbench

Funcionalidades

    Agendamento de consultas
    Cadastro de pacientes e médicos
    Visualização e gerenciamento de consultas
    Interface responsiva e acessível em dispositivos móveis

Instalação

    Clone o repositório:
    
    git clone https://github.com/usuario/nome-do-repositorio.git

    bash


Navegue para o diretório do projeto:

    cd nome-do-repositorio

Crie um ambiente virtual e ative-o:

    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`

Instale as dependências:

    pip install -r requirements.txt

Configure o banco de dados no arquivo settings.py e aplique as migrações:

    python manage.py migrate

Inicie o servidor de desenvolvimento:

    python manage.py runserver
