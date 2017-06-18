# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('municipios', '__first__'),
        ('core', '0002_delete_developer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('cep', models.CharField(max_length=9)),
                ('logradouro', models.CharField(max_length=100)),
                ('numero', models.CharField(max_length=50, verbose_name='N\xfamero')),
                ('complemento', models.CharField(max_length=100, null=True, blank=True)),
                ('bairro', models.CharField(max_length=100)),
                ('municipio', models.ForeignKey(to='municipios.Municipio')),
            ],
            options={
                'verbose_name': 'Endere\xe7o',
            },
        ),
    ]
