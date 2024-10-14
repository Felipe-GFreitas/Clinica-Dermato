# Generated by Django 5.1.1 on 2024-10-14 01:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicos',
            name='crm',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='medicos',
            name='especialidade',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='medicos',
            name='horario',
            field=models.CharField(choices=[('manha', 'Manhã'), ('tarde', 'Tarde'), ('integral', 'Integral')], max_length=10),
        ),
        migrations.AlterField(
            model_name='medicos',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='nome',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='pacientes',
            name='telefone',
            field=models.CharField(max_length=15),
        ),
        migrations.CreateModel(
            name='Consultas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_consulta', models.DateField()),
                ('hora_consulta', models.TimeField()),
                ('status', models.CharField(choices=[('agendada', 'Agendada'), ('concluida', 'Concluída'), ('cancelada', 'Cancelada')], default='agendada', max_length=10)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.medicos')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pacientes')),
            ],
            options={
                'unique_together': {('medico', 'data_consulta', 'hora_consulta')},
            },
        ),
    ]