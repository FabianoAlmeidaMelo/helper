# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0011_auto_20160128_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarefa',
            name='parcela',
        ),
    ]
