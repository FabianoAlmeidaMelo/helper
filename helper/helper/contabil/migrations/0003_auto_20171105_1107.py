# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0006_auto_20171008_2240'),
        ('contabil', '0002_contador_endereco'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContaMensagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('data', models.DateTimeField(null=True, blank=True)),
                ('conta', models.ForeignKey(to='core.Conta')),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_upd', models.DateTimeField(auto_now=True)),
                ('texto', models.TextField(verbose_name='Texto')),
                ('contas', models.ManyToManyField(to='core.Conta', through='contabil.ContaMensagem')),
                ('setor', models.ForeignKey(to='contabil.Setor')),
                ('user_add', models.ForeignKey(related_name='contabil_mensagem_created_by', to=settings.AUTH_USER_MODEL)),
                ('user_upd', models.ForeignKey(related_name='contabil_mensagem_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='contamensagem',
            name='mensagem',
            field=models.ForeignKey(to='contabil.Mensagem'),
        ),
        migrations.AddField(
            model_name='contamensagem',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
