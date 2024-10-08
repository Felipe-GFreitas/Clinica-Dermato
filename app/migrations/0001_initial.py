# Generated by Django 5.1.1 on 2024-09-29 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('crm', models.CharField(max_length=11)),
                ('especialidade', models.CharField(max_length=30)),
                ('horario', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('telefone', models.CharField(max_length=30)),
                ('cpf', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=100)),
                ('data_nascimento', models.DateField()),
            ],
        ),
    ]
