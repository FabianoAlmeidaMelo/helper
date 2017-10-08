# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_conta'),
        ('agenda', '0006_auto_20171007_2057'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='conta_core',
            field=models.ForeignKey(to='core.Conta', null=True),
        ),
    ]
