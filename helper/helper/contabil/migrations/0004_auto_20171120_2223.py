# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import helper.contabil.models


class Migration(migrations.Migration):

    dependencies = [
        ('contabil', '0003_auto_20171105_1107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mensagem',
            options={'ordering': ('-date_upd',)},
        ),
        migrations.AddField(
            model_name='mensagem',
            name='filename',
            field=models.FileField(max_length=300, upload_to=helper.contabil.models.user_directory_path, null=True, verbose_name='Anexo', blank=True),
        ),
    ]
