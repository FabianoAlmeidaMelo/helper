# coding: utf-8
from django.db import models

from helper.core.models import User

TIPO = (
    (1, u'Bronze'),
    (2, u'Prata'),
    (3, u'Ouro'),
    )


class Conta(models.Model):
    dono = models.ForeignKey(User)
    tipo = models.SmallIntegerField(u'tipo', choices=TIPO)
    valor = models.DecimalField(
                                u'Valor',
                                max_digits=7,
                                decimal_places=2,
                                blank=True,
                                null=True
                                )
    validade = models.DateTimeField(u'Data')

    class Meta:
        verbose_name = u'Conta'
        verbose_name_plural = u'Contas'

    def __unicode__(self):
        return self.titulo


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
        ordering = ['data_ini', 'hora_ini']

    def __unicode__(self):
        return self.titulo


# class Categoria(models.Model):
#     agenda = models.ForeignKey(Agenda)
#     nome = models.CharField(u'Nome', max_length=200)
