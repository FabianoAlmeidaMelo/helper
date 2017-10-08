# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0005_auto_20170618_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servico',
            options={'ordering': ('agenda__nome', 'id'), 'verbose_name': 'Servi\xe7o', 'verbose_name_plural': 'Servi\xe7os'},
        ),
        migrations.AlterField(
            model_name='agenda',
            name='tipo',
            field=models.SmallIntegerField(default=2, verbose_name='Tipo', choices=[(1, 'Pessoa Jur\xeddica'), (2, 'Pessoa F\xedsica')]),
        ),
    ]
