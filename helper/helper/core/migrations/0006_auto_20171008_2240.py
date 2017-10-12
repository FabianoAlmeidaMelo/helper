# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_conta'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='conta',
            field=models.ForeignKey(to='core.Conta', null=True),
        ),
        migrations.AlterField(
            model_name='conta',
            name='dono',
            field=models.ForeignKey(related_name='dono_conta_core', to=settings.AUTH_USER_MODEL),
        ),
    ]
