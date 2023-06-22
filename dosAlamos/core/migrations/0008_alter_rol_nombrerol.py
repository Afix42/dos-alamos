# Generated by Django 4.0.4 on 2023-06-21 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_horatomada_correopaciente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rol',
            name='nombreRol',
            field=models.CharField(choices=[('Paciente', 'Paciente'), ('Medico', 'Medico'), ('Secretaria', 'Secretaria')], default='Paciente', max_length=25, verbose_name='El nombre del rol de usuario'),
        ),
    ]