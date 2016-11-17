# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user'),
        ('agenda', '0002_tarefa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.SmallIntegerField(verbose_name='tipo', choices=[(1, 'Bronze'), (2, 'Prata'), (3, 'Ouro')])),
                ('valor', models.DecimalField(null=True, verbose_name='Valor', max_digits=7, decimal_places=2, blank=True)),
                ('validade', models.DateTimeField(verbose_name='Data')),
                ('dono', models.ForeignKey(to='core.User')),
            ],
            options={
                'verbose_name': 'Conta',
                'verbose_name_plural': 'Contas',
            },
        ),
    ]
