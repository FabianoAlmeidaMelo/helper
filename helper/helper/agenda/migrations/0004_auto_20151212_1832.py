# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0003_conta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('observacao', models.TextField(null=True, blank=True)),
                ('conta', models.ForeignKey(to='agenda.Conta')),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
            },
        ),
        migrations.AlterModelOptions(
            name='tarefa',
            options={'ordering': ['data_ini', 'hora_ini'], 'verbose_name': 'Tarefa', 'verbose_name_plural': 'Tarefas'},
        ),
    ]
