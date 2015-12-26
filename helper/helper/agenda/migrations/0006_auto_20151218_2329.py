# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_servico'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='servico',
            field=models.ForeignKey(blank=True, to='agenda.Servico', null=True),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='titular',
            field=models.ForeignKey(blank=True, to='core.User', null=True),
        ),
    ]
