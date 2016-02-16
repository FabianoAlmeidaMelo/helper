# coding: utf-8
from django.db import models
from django.core.exceptions import ValidationError
from datetime import date, datetime
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

TIPO_CHOICES = (
    (0, '---'),
    (1, u'(+)'),
    (2, u'(-)'),
    )


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
    usuario = models.ForeignKey(User)
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

    @property
    def get_data_vencimento(self):
        '''
        retorna a data de pagar o cartão
        no mês corrente
        '''
        hoje = date.today()
        return datetime(hoje.year, hoje.month, self.vencimento)

    @property
    def get_data_fechamento(self):
        '''
        retorna a data de fechamento da fatura
        no mês corrente
        '''

        hoje = date.today()
        return datetime(hoje.year, hoje.month, self.fechamento)

    def get_data_fechamento_mes(self, data):
        '''
        retorna a data de fechamento da fatura
        a partir de uma data
        '''
        return date(data.year, data.month, self.fechamento)

    def get_data_pagamento_mes(self, data):
        '''
        retorna a data de fechamento da fatura
        a partir de uma data
        '''
        data_fechamento = self.get_data_fechamento_mes(data)
        if data < data_fechamento:
            return date(data.year, data.month, self.vencimento)
        elif data.month == 12:
            return date(data.year + 1, 1, self.vencimento)
        else:
            return date(data.year, data.month + 1, self.vencimento)


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
    cartao = models.ForeignKey(CartaoCredito, null=True, blank=True)
    tipo = models.SmallIntegerField(
                                    u"Tipo",
                                    choices=TIPO_CHOICES,
                                    null=True,
                                    blank=True
                                )
    parcela = models.ForeignKey(
                                'Tarefa',
                                null=True,
                                blank=True
                            )
    nr_parcela = models.PositiveSmallIntegerField(
                                           u'Nr de Parcelas',
                                           null=True,
                                           blank=True
                                    )

    class Meta:
        verbose_name = u'Tarefa'
        verbose_name_plural = u'Tarefas'
        ordering = ['data_ini', 'hora_ini']

    def __unicode__(self):
        return self.titulo

    def set_data_parcela_mae(self):
        '''
        ref #17
        deve setar a data inicial de Tarefa
        '''
        cartao = self.cartao
        data_ini = self.data_ini

        if cartao and self.pago is not True and self.parcela is None:
            self.data_ini = cartao.get_data_pagamento_mes(data_ini)
            self.descricao += '\n\n **Data da compra %s:' % data_ini
        return self

    def set_data_parcela_filha(self):
        '''
        basear na data da parcela mãe;
        no em um count no 'for', para saber que parcela é.
        '''
        last_sum = self.tarefa_set.all().last()
        last_sum_data_ini = last_sum.data_ini if last_sum else self.data_ini

        return self.cartao.get_data_pagamento_mes(last_sum_data_ini)

    def list_parcelas(self):
        '''
        talvez esse metodo escolha,
            Se chama metodo que cria OU
            Se chama metodo que edita
        '''
        if self.tarefa_set.all().count() != self.nr_parcela:
            self.tarefa_set.all().delete()
        return range(1, self.nr_parcela)

    def set_parcela_filha(self):
        '''
        risco, na edição criar infinitas parcelas ...
        comparar com o nr de parcelas
        se tiver menos, apaga o excesso
        '''
        parcelas = self.list_parcelas()
        valor = self.valor/self.nr_parcela
        for parcela in parcelas:
            t = Tarefa()  # melhor get_or_create pela data_ini!!
            t.servico = self.servico
            t.titular = self.titular
            t.titulo = self.titulo + u': ' + str(parcela + 1) + u' / ' + str(len(parcelas))
            t.descricao = self.descricao
            t.tipo = self.tipo
            t.descricao += u'\n\n%s - Parcela nr: %s de %s' % (valor, (parcela + 1), str(self.nr_parcela))
            t.data_ini = self.set_data_parcela_filha()
            t.hora_ini = self.hora_ini
            t.data_fim = self.data_fim
            t.hora_fim = self.hora_fim
            t.confirmado = self.confirmado
            t.valor = self.valor
            t.parcela = self
            t.valor = valor  # dividido ...
            t.pago = None
            t.cartao = self.cartao
            t.parcela = self
            t.save()
            print t.data_ini
        self.titulo + u': 1ª de %s' % self.nr_parcela
        self.valor = valor
        self.save()


    # def set_parcela_filha(self, nr_parcelas=1):
    #     '''
    #     risco, na edição criar infinitas parcelas ...
    #     '''
    #     parcelas = range(1, nr_parcelas)
    #     valor = self.valor/nr_parcelas
    #     for parcela in parcelas:
    #         t = Tarefa()  # melhor get_or_create pela data_ini!!
    #         t.servico = self.servico
    #         t.titular = self.titular
    #         t.titulo = self.titulo + u': ' + str(parcela + 1)
    #         t.descricao = self.descricao
    #         t.tipo = self.tipo
    #         t.descricao += u'\n\n%s - Parcela nr: %s de %s' % (valor, (parcela + 1), nr_parcelas)
    #         t.data_ini = self.set_data_parcela_filha()
    #         t.hora_ini = self.hora_ini
    #         t.data_fim = self.data_fim
    #         t.hora_fim = self.hora_fim
    #         t.confirmado = self.confirmado
    #         t.valor = self.valor
    #         t.parcela = self
    #         t.valor = valor  # dividido ...
    #         t.pago = None
    #         t.cartao = self.cartao
    #         t.parcela = self
    #         t.save()
    #         print t.data_ini
    #     self.titulo + u': 1ª de %s' % nr_parcelas
    #     self.valor = valor
    #     self.save()
