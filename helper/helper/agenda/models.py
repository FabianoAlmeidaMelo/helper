# coding: utf-8
from django.db import models
from django.core.exceptions import ValidationError

from helper.core.models import User

TIPO = (
    (1, u'Bronze'),
    (2, u'Prata'),
    (3, u'Ouro'),
    )

CARTAO_CHOICES = (
    (1, 'Visa'),
    (2, 'Master Card'),
    (3, 'Amex'),
    (4, 'Outros'),
    )

# AGENDA_PERMISSAO = (
#     (1, u'Create'),
#     (2, u'Read'),
#     (3, u'Edit'),
#     (4, u'Delete'),
#     )


def validate_vencimento(value):
    if value not in range(1, 29):
        raise ValidationError(u'%s Não está entre 1 e 28' % value)


def validate_fechamento(value):
    if value not in range(1, 29):
        raise ValidationError(u'%s Não está entre 1 e 31' % value)


class Conta(models.Model):
    """
    Uma pessoa física ou jurídica pode ter N Contas
    cada Conta pode ter N agendas
    as contas devem ter mais ou menos benefícios, de
    acordo com o Tipo.
    TODO:
        Levar para app core ?
    """
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
        return self.dono.nome


class CartaoCredito(models.Model):
    '''
    ref #14
    TODO
        levar par uma app:
            'acessorio'?
            'meios'?
        de Pagamentos $ -->
        pode ter de Recebimentos <-- $
            é um atributo tipo?
            acho que não, varia de acordo com contrato das Operadoras E
            Banco Intermediário
    '''
    conta = models.ForeignKey(Conta)
    bandeira = models.SmallIntegerField(u"Bandeira", choices=CARTAO_CHOICES)
    vencimento = models.IntegerField(
                                     u'Dia de Pagar',
                                     validators=[validate_vencimento],
                                )
    fechamento = models.IntegerField(
                                     u'Dia do Fechamento',
                                     validators=[validate_fechamento],
                                     null=True,
                                     blank=True
                                )
    limite = models.DecimalField(
                                u'Limite $',
                                max_digits=7,
                                decimal_places=2,
                                blank=True,
                                null=True
                            )

    def __unicode__(self):
        return self.get_bandeira_display()


class Agenda(models.Model):
    '''
    agenda:
      Fzda Vera Cruz
      ZNC
      Helper
    '''
    conta = models.ForeignKey(Conta)
    nome = models.CharField(u'Nome', max_length=200)
    observacao = models.TextField(null=True, blank=True)
    # agenda_usuario = models.ManyToManyField(User, through='AgendaUsuario')

    class Meta:
        verbose_name = u'Agenda'
        verbose_name_plural = u'Agendas'

    def __unicode__(self):
        return self.nome


class Servico(models.Model):
    '''
    servico:
        locacacao_fazda
        tirolesa
        quartos_externos
        salao_festa
    '''
    agenda = models.ForeignKey(Agenda)
    nome = models.CharField(u'Nome', max_length=200)

    def __unicode__(self):
        return u"%s - %s" % (self.agenda, self.nome)

    class Meta:
        ordering = ('agenda__nome', 'nome',)


class Tarefa(models.Model):
    """
    #12
    TODO
        se serviço é None, de qual agenda e conta é essa tarefa???
    """
    servico = models.ForeignKey(Servico, null=True, blank=True)
    titular = models.ForeignKey(User, null=True, blank=True)
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
