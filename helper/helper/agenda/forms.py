# coding: utf-8
from decimal import Decimal
from datetime import date
from django import forms
from django.db.models import Q

from .models import (
    Agenda,
    CartaoCredito,
    Servico,
    Tarefa,
)
from helper.core.forms import BaseSearchForm
from bootstrap_toolkit.widgets import BootstrapDateInput


class AgendaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.conta = kwargs.pop('conta', None)
        super(AgendaForm, self).__init__(*args, **kwargs)

    def save(self):
        self.instance.conta = self.conta
        self.instance.save()

    class Meta:
        model = Agenda
        fields = ('nome',
                  'observacao',
                  'tipo')


class CartaoCreditoForm(forms.ModelForm):
    '''
    Cartao é o do dono da Conta, um User
    pode estar vinculado a mais de 1 agenda
    '''
    def __init__(self, *args, **kargs):
        self.conta = kargs.pop('conta', None)
        super(CartaoCreditoForm, self).__init__(*args, **kargs)

    class Meta:
        model = CartaoCredito
        fields = (
                    'usuario',  # TODO remover, é o dono da conta
                    'bandeira',
                    'vencimento',
                    'fechamento',
                    'limite',
                    'ativo',
                    )


class CartaoCreditoBaseSearchForm(BaseSearchForm):

    class Meta:
        base_qs = CartaoCredito.objects
        search_fields = (
                          'bandeira',
                          'fechamento',
                          'vencimento',
                    )


class ServicoForm(forms.ModelForm):

    class Meta:
        model = Servico
        fields = (
                    'nome',
                    'agenda',
                    )


class TarefaForm(forms.ModelForm):
    nr_parcela = forms.IntegerField(label='Nr de Parcelas', required=False)
    data_ini = forms.DateField(
                                label='Data Inicial',
                                widget=BootstrapDateInput,
                                required=True
                            ) 
    data_fim = forms.DateField(
                                label='Data Final',
                                widget=BootstrapDateInput,
                                required=False
                            ) 

    def __init__(self, *args, **kargs):
        self.user = kargs.pop('user', None)
        self.agenda = kargs.pop('agenda', None)
        super(TarefaForm, self).__init__(*args, **kargs)
        self.fields['parcela'].widget = forms.HiddenInput()
        self.fields['cartao'].queryset = CartaoCredito.objects.filter(ativo=True)

        self.fields['servico'].required = True

    def clean_valor(self):
        '''#20
        se tiver nr + nr_parcela
        e não tiver valor, vai dividir Zero por nr_parcela
        e não por None
        '''
        valor = self.cleaned_data['valor'] or Decimal('0')
        return valor

    def save(self, *args, **kargs):
        is_new = self.instance.pk is None
        data_ini = None

        if is_new is False:  # data_ini No BD
            data_ini = Tarefa.objects.get(id=self.instance.pk).data_ini
        data_ini_form = self.cleaned_data['data_ini']
        instance = super(TarefaForm, self).save(*args, **kargs)

        if data_ini != data_ini_form:
            nr_parcela = self.cleaned_data['nr_parcela'] or 1
            if all(
                    [instance.pago is not True,
                     int(nr_parcela) >= 1,
                     instance.parcela is None]):
                instance.set_data_parcela_mae()
            instance.save()
            if self.instance.nr_parcela:
                instance.set_parcela_filha()
        else:
            instance.save()
        return instance

    class Meta:
        model = Tarefa
        fields = (
                    'servico',
                    'titulo',
                    'descricao',
                    'data_ini',
                    'data_fim',
                    'hora_ini',
                    'hora_fim',
                    'confirmado',
                    'valor',
                    'pago',
                    'tipo',
                    'cartao',
                    'parcela',
                    'nr_parcela',
                    'nr_documento',
                    )


TIPO_CHOICES = (
    ('', '---'),
    (1, u'(+)'),
    (2, u'(-)'),
    )


class TarefaSearchForm(BaseSearchForm):
    '''
    #12
    '''
    servico = forms.CharField(label=u'Servico', required=False)
    titulo = forms.CharField(label=u'Título', required=False)
    descricao = forms.CharField(label=u'Descrição', required=False)
    data_ini = forms.DateField(
                                label='Data Inicial',
                                widget=BootstrapDateInput,
                                required=False
                            )
    data_fim = forms.DateField(
                                label='Data Final',
                                widget=BootstrapDateInput,
                                required=False
                            )
    confirmado = forms.BooleanField(label='Confirmado', required=False)
    pago = forms.BooleanField(label='Pago', required=False)
    not_pago = forms.BooleanField(label='Não Pago', required=False)
    hoje = forms.BooleanField(label='Hoje e não pagas ...', required=False, initial=True)
    tipo = forms.ChoiceField(
                             label='Tipo',
                             choices=TIPO_CHOICES,
                             required=False                            
                        )
    valor = forms.DecimalField(
                                u'Valor',
                                required=False
                        )

    def __init__(self, *args, **kwargs):
        super(TarefaSearchForm, self).__init__(*args, **kwargs)
        self.fields['q'].widget.attrs['placeholder'] = u'Agenda, Nome do serviço, Título, Descrição'
        # self.fields['hoje'].widget=forms.CheckboxInput(attrs={'checked' : 'checked'})

    def prepare_data_ini(self):
        data_ini = self.cleaned_data['data_ini']  # or date.today()
        if data_ini:
            return Q(data_ini__gte=data_ini)
        return

    def prepare_data_fim(self):
        data_fim = self.cleaned_data['data_fim']
        if data_fim:
            return Q(data_ini__lte=data_fim)
        return

    def prepare_hoje(self):
        # import pdb; pdb.set_trace()
        hoje = self.cleaned_data['hoje']
        if hoje:
            return  Q(pago=False) | Q(pago__isnull=True) | Q(data_ini=date.today())
        return

    def prepare_confirmado(self):
        confirmado = self.cleaned_data['confirmado']
        if confirmado:
            return Q(confirmado=confirmado)
        return

    def prepare_pago(self):
        pago = self.cleaned_data['pago']
        if pago:
            return Q(pago=pago)
        return

    def prepare_tipo(self):
        tipo = self.cleaned_data['tipo']
        if tipo:
            return Q(tipo=tipo)
        return

    def prepare_not_pago(self):
        not_pago = self.cleaned_data['not_pago']
        if not_pago:
            return Q(pago=False) | Q(pago__isnull=True)
        return

    def prepare_valor(self):
        valor = self.cleaned_data['valor']
        if valor:
            return Q(valor__icontains=valor)
        return

    class Meta:
        base_qs = Tarefa.objects
        search_fields = (
                          'servico__nome',
                          'titulo',
                          'descricao',
                          'servico__agenda__nome',
                          'nr_documento',
                    )

    # def get_result_queryset(self):
    #     # import pdb; pdb.set_trace()
    #     q = Q(data_ini__gte=date.today()) | Q(pago=False) | Q(pago=None)
    #     if self.is_valid():
    #         # q = Q()
    #         servico = self.cleaned_data['servico']
    #         if servico:
    #             q = q & Q(servico__nome__icontains=servico)
    #         titulo = self.cleaned_data['titulo']
    #         if titulo:
    #             q = q & Q(titulo__icontains=titulo)
    #         descricao = self.cleaned_data['descricao']
    #         if descricao:
    #             q = q & Q(descricao__icontains=descricao)
    #         data_ini = self.cleaned_data['data_ini']
    #         if data_ini:
    #             q = q & Q(data_ini__gte=data_ini)
    #         data_fim = self.cleaned_data['data_fim']
    #         if data_fim:
    #             q = q & Q(data_ini__lte=data_ini)
    #         confirmado =     #             q = q & Q(confirmado=True)
    #         pago = self.cleaned_data['pago']
    #         if pago:
    #             q = q & Q(pago=True)

    #         return Tarefa.objects.filter(q)
    #     return Tarefa.objects.filter(q)
