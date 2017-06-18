# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabil', '0001_initial'),
        ('agenda', '0003_tarefa_nr_documento'),
    ]

    operations = [
        migrations.AddField(
            model_name='conta',
            name='contador',
            field=models.ForeignKey(blank=True, to='contabil.Contador', null=True),
        ),
        migrations.AlterField(
            model_name='conta',
            name='tipo',
            field=models.SmallIntegerField(verbose_name='tipo', choices=[(1, 'Contador'), (2, 'Empresarial'), (3, 'Ouro')]),
        ),
    ]
