# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0010_auto_20171012_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agenda',
            name='conta_core',
        ),
        migrations.AlterField(
            model_name='agenda',
            name='conta',
            field=models.ForeignKey(to='core.Conta', null=True),
        ),
    ]
