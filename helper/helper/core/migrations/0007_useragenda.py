# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0011_auto_20171012_1753'),
        ('core', '0006_auto_20171008_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAgenda',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('agenda', models.ForeignKey(to='agenda.Agenda')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
