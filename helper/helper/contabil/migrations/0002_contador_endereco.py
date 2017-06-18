# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contabil', '0001_initial'),
        ('core', '0003_endereco'),
    ]

    operations = [
        migrations.AddField(
            model_name='contador',
            name='endereco',
            field=models.ForeignKey(blank=True, to='core.Endereco', null=True),
        ),
    ]
