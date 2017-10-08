# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contabil', '0002_contador_endereco'),
        ('core', '0004_auto_20170617_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipo', models.SmallIntegerField(verbose_name='tipo', choices=[(1, 'Contador'), (2, 'Empresarial'), (3, 'Outra')])),
                ('valor', models.DecimalField(null=True, verbose_name='Valor', max_digits=7, decimal_places=2, blank=True)),
                ('validade', models.DateTimeField(verbose_name='Data')),
                ('contador', models.ForeignKey(related_name='conta_core', blank=True, to='contabil.Contador', null=True)),
                ('dono', models.ForeignKey(related_name='conta_core', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Conta',
                'verbose_name_plural': 'Contas',
            },
        ),
    ]
