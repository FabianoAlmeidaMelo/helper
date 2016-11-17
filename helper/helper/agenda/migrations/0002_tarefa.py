# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user'),
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=255, verbose_name='T\xedtulo')),
                ('descricao', models.TextField(verbose_name='Descri\xe7\xe3o')),
                ('data_ini', models.DateField(verbose_name='Data')),
                ('hora_ini', models.TimeField(verbose_name='Hora')),
                ('data_fim', models.DateField(null=True, verbose_name='Data Final', blank=True)),
                ('hora_fim', models.TimeField(null=True, verbose_name='Hora Final', blank=True)),
                ('confirmado', models.NullBooleanField(verbose_name='Confirmado')),
                ('valor', models.DecimalField(null=True, verbose_name='Valor', max_digits=7, decimal_places=2, blank=True)),
                ('pago', models.NullBooleanField(verbose_name='Pago')),
                ('titular', models.ForeignKey(to='core.User')),
            ],
            options={
                'verbose_name': 'Tarefa',
                'verbose_name_plural': 'Tarefas',
            },
        ),
    ]
