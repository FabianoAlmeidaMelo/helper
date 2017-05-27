# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_cartaocredito_ativo'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='nr_documento',
            field=models.CharField(max_length=20, null=True, verbose_name='Nr Documento', blank=True),
        ),
    ]
