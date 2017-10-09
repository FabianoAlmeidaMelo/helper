# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0008_auto_20171007_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conta',
            name='dono',
            field=models.ForeignKey(related_name='dono_conta_agenda', to=settings.AUTH_USER_MODEL),
        ),
    ]
