# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import helper.agenda.models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_auto_20151218_2329'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartaoCredito',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bandeira', models.SmallIntegerField(verbose_name='Bandeira', choices=[(1, b'Visa'), (2, b'Master Card'), (3, b'Amex'), (4, b'Outros')])),
                ('vencimento', models.IntegerField(verbose_name='Dia de Pagar', validators=[helper.agenda.models.validate_vencimento])),
                ('fechamento', models.IntegerField(blank=True, null=True, verbose_name='Dia do Fechamento', validators=[helper.agenda.models.validate_fechamento])),
                ('limite', models.DecimalField(null=True, verbose_name='Limite $', max_digits=7, decimal_places=2, blank=True)),
                ('conta', models.ForeignKey(to='agenda.Conta')),
            ],
        ),
        migrations.AlterModelOptions(
            name='servico',
            options={'ordering': ('agenda__nome', 'nome')},
        ),
    ]
