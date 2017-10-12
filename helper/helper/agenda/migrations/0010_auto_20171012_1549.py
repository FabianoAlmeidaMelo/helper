# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0009_auto_20171008_2240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='conta',
            name='contador',
        ),
        migrations.RemoveField(
            model_name='conta',
            name='dono',
        ),
        migrations.DeleteModel(
            name='Conta',
        ),
    ]
