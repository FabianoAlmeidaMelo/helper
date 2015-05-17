# coding: utf-8

from django.db import models


class Developer(models.Model):
    name = models.CharField(verbose_name=u'Nome', max_length=255)
