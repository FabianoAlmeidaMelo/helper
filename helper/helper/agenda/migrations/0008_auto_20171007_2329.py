# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0007_agenda_conta_core'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='conta',
            field=models.ForeignKey(related_name='core', to='core.Conta', null=True),
        ),
    ]
