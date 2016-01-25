# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_user'),
        ('agenda', '0007_auto_20160119_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartaocredito',
            name='usuario',
            field=models.ForeignKey(default=1, to='core.User'),
            preserve_default=False,
        ),
    ]
