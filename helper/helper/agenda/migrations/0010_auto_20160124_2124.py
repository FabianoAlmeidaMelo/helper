# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0009_remove_cartaocredito_conta'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='cartao',
            field=models.ForeignKey(blank=True, to='agenda.CartaoCredito', null=True),
        ),
        migrations.AddField(
            model_name='tarefa',
            name='tipo',
            field=models.SmallIntegerField(blank=True, null=True, verbose_name='Tipo', choices=[(1, 'Recebimento'), (2, 'Pagamento')]),
        ),
    ]
