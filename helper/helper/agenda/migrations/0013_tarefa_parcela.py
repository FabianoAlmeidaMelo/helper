# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0012_remove_tarefa_parcela'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='parcela',
            field=models.ForeignKey(blank=True, to='agenda.Tarefa', null=True),
        ),
    ]
