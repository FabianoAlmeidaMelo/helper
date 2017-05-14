# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import helper.agenda.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('observacao', models.TextField(null=True, verbose_name=b'observa\xc3\xa7\xc3\xa3o', blank=True)),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
            },
        ),
        migrations.CreateModel(
            name='CartaoCredito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bandeira', models.SmallIntegerField(verbose_name='Bandeira', choices=[(1, b'Visa'), (2, b'Master Card'), (3, b'Amex'), (4, b'Outros')])),
                ('vencimento', models.IntegerField(verbose_name='Dia de Pagar', validators=[helper.agenda.models.validate_vencimento])),
                ('fechamento', models.IntegerField(blank=True, null=True, verbose_name='Dia do Fechamento', validators=[helper.agenda.models.validate_fechamento])),
                ('limite', models.DecimalField(null=True, verbose_name='Limite $', max_digits=7, decimal_places=2, blank=True)),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.SmallIntegerField(verbose_name='tipo', choices=[(1, 'Bronze'), (2, 'Prata'), (3, 'Ouro')])),
                ('valor', models.DecimalField(null=True, verbose_name='Valor', max_digits=7, decimal_places=2, blank=True)),
                ('validade', models.DateTimeField(verbose_name='Data')),
                ('dono', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Conta',
                'verbose_name_plural': 'Contas',
            },
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200, verbose_name='Nome')),
                ('agenda', models.ForeignKey(to='agenda.Agenda')),
            ],
            options={
                'ordering': ('agenda__nome', 'nome'),
            },
        ),
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
                ('tipo', models.SmallIntegerField(blank=True, null=True, verbose_name='Tipo', choices=[(1, '(+)'), (2, '(-)')])),
                ('nr_parcela', models.PositiveSmallIntegerField(null=True, verbose_name='Nr de Parcelas', blank=True)),
                ('cartao', models.ForeignKey(blank=True, to='agenda.CartaoCredito', null=True)),
                ('parcela', models.ForeignKey(blank=True, to='agenda.Tarefa', null=True)),
                ('servico', models.ForeignKey(blank=True, to='agenda.Servico', null=True)),
                ('titular', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ['data_ini', 'hora_ini'],
                'verbose_name': 'Tarefa',
                'verbose_name_plural': 'Tarefas',
            },
        ),
        migrations.AddField(
            model_name='agenda',
            name='conta',
            field=models.ForeignKey(to='agenda.Conta'),
        ),
    ]
