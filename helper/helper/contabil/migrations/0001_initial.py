# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('cnpj', models.CharField(max_length=18, verbose_name='CNPJ')),
                ('telefone', models.CharField(max_length=14, null=True, verbose_name='Telefone', blank=True)),
                ('telefone2', models.CharField(max_length=14, null=True, verbose_name='Telefone 2', blank=True)),
                ('celular', models.CharField(max_length=14, null=True, verbose_name='Celular', blank=True)),
                ('email', models.EmailField(max_length=50, null=True, verbose_name='email', blank=True)),
                ('nome_contato', models.CharField(max_length=200, verbose_name='Nome do Contato')),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('contador', models.ForeignKey(to='contabil.Contador')),
            ],
        ),
        migrations.CreateModel(
            name='SetorContato',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefone', models.CharField(max_length=14, null=True, verbose_name='Telefone', blank=True)),
                ('email', models.EmailField(max_length=50, null=True, verbose_name='email', blank=True)),
                ('nome_contato', models.CharField(max_length=60)),
                ('setor', models.ForeignKey(to='contabil.Setor')),
            ],
        ),
        migrations.CreateModel(
            name='SetorUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('setor', models.ForeignKey(to='contabil.Setor')),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
