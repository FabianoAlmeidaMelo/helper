# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name=b'e-mail')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('is_active', models.BooleanField(default=True, verbose_name=b'ativo')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'data de cadastro')),
                ('nascimento', models.DateField(null=True, verbose_name='Data Nascimento', blank=True)),
                ('profissao', models.CharField(max_length=100, null=True, verbose_name='Profiss\xe3o', blank=True)),
                ('sexo', models.IntegerField(blank=True, null=True, verbose_name='Sexo', choices=[(1, b'M'), (2, b'F')])),
            ],
            options={
                'verbose_name': 'Usu\xe1rio',
                'verbose_name_plural': 'Usu\xe1rios',
            },
        ),
    ]
