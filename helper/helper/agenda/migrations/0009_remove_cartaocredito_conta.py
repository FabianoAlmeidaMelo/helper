# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0008_cartaocredito_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartaocredito',
            name='conta',
        ),
    ]
