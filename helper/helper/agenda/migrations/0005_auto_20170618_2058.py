# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_auto_20170617_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='tipo',
            field=models.SmallIntegerField(default=2, verbose_name='Tipo', choices=[(1, 'Pessoa Jur\xeddica'), (2, 'Pessoa F\xedsica')]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conta',
            name='tipo',
            field=models.SmallIntegerField(verbose_name='tipo', choices=[(1, 'Contador'), (2, 'Empresarial'), (3, 'Outra')]),
        ),
    ]
