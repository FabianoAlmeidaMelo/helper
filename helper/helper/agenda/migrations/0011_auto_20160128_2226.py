# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0010_auto_20160124_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='parcela',
            field=models.SmallIntegerField(null=True, verbose_name='Nr Parcelas', blank=True),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='tipo',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Tipo', choices=[(0, b'---'), (1, '(+)'), (2, '(-)')]),
        ),
    ]
