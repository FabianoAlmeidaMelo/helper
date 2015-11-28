# coding: utf-8
from django.db import models

from helper.core.models import User


class Tarefa(models.Model):
    """
    #12
    """
    titular = models.ForeignKey(User)
    titulo = models.CharField(verbose_name=u'Título', max_length=255)
    descricao = models.TextField(verbose_name=u'Descrição')
    data_ini = models.DateField(u'Data')
    hora_ini = models.TimeField(u'Hora')
    data_fim = models.DateField(u'Data Final', null=True, blank=True)
    hora_fim = models.TimeField(u'Hora Final', null=True, blank=True)
    confirmado = models.NullBooleanField(u'Confirmado')
    valor = models.DecimalField(
                                u'Valor',
                                max_digits=7,
                                decimal_places=2,
                                blank=True,
                                null=True
                                )
    pago = models.NullBooleanField(u'Pago')

    class Meta:
        verbose_name = u'Tarefa'
        verbose_name_plural = u'Tarefas'

    def __unicode__(self):
        return self.titulo
