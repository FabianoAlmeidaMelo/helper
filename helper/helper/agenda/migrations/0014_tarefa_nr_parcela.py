# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0013_tarefa_parcela'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='nr_parcela',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Nr da Parcela', blank=True),
        ),
    ]
