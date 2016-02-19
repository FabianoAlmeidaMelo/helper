# coding: utf-8
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
        super(AgendaForm, self).__init__(*args, **kwargs)

    def save(self):
        self.conta = self.user.conta_set.all().last()
        self.instance.save()

    class Meta:
        model = Agenda
        fields = (
                    'nome',
                    'observacao',
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

    def __init__(self, *args, **kargs):
        self.user = kargs.pop('user', None)
        self.agenda = kargs.pop('agenda', None)
        super(TarefaForm, self).__init__(*args, **kargs)
        self.fields['parcela'].widget = forms.HiddenInput()
        self.fields['cartao'].queryset = CartaoCredito.objects.filter()

        self.fields['servico'].required = True
        # if any([
        #         self.instance.cartao,
        #         self.instance.valor,
        #         self.instance.tipo]):
        #     self.fields['tipo'].required = True
        #     self.fields['valor'].required = True

    def save(self, *args, **kargs):
        is_new = self.instance.pk is None
        data_ini = None

        if is_new is False:  # data_ini No BD
            data_ini = Tarefa.objects.get(id=self.instance.pk).data_ini
        data_ini_form = self.cleaned_data['data_ini']
        instance = super(TarefaForm, self).save(*args, **kargs)

        if data_ini != data_ini_form:
            if instance.cartao and instance.pago is not True:
                instance.set_data_parcela_mae()
        instance.save()
        nr_parcela = self.cleaned_data['nr_parcela'] or 1
        if instance.cartao and nr_parcela > 1:
            instance.set_parcela_filha()
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
                                required=False,
                                )
    data_fim = forms.DateField(
                                label='Data Final',
                                widget=BootstrapDateInput,
                                required=False
                                )
    confirmado = forms.BooleanField(label='Confirmado', required=False)
    pago = forms.BooleanField(label='Pago', required=False)

    def get_result_queryset(self):

        q = Q()
        if self.is_valid():
            servico = self.cleaned_data['servico']
            if servico:
                q = q & Q(servico__nome__icontains=servico)
            titulo = self.cleaned_data['titulo']
            if titulo:
                q = q & Q(titulo__icontains=titulo)
            descricao = self.cleaned_data['descricao']
            if descricao:
                q = q & Q(descricao__icontains=descricao)

            data_ini = self.cleaned_data['data_ini']
            if data_ini:
                q = q & Q(data_ini__gte=data_ini)
            data_fim = self.cleaned_data['data_fim']
            if data_fim:
                q = q & Q(data_ini__lte=data_fim)
            confirmado = self.cleaned_data['confirmado']
            if confirmado:
                q = q & Q(confirmado=True)
            pago = self.cleaned_data['pago']
            if pago:
                q = q & Q(pago=True)

            return Tarefa.objects.filter(q)
        return Tarefa.objects.filter(data_ini__gte=date.today())

    class Meta:
        base_qs = Tarefa.objects
        search_fields = ('servico__nome', 'titulo', 'descricao')



# class TarefaSearchForm(forms.Form):
#     '''
#     #12
#     '''
#     servico = forms.CharField(label=u'Servico', required=False)
#     titulo = forms.CharField(label=u'Título', required=False)
#     descricao = forms.CharField(label=u'Descrição', required=False)
#     data_ini = forms.DateField(
#                                 label='Data Inicial',
#                                 widget=BootstrapDateInput,
#                                 required=False
#                                 )
#     data_fim = forms.DateField(
#                                 label='Data Final',
#                                 widget=BootstrapDateInput,
#                                 required=False
#                                 )
#     confirmado = forms.BooleanField(label='Confirmado', required=False)
#     pago = forms.BooleanField(label='Pago', required=False)

#     def get_result_queryset(self):
#         # import pdb; pdb.set_trace()
#         q = Q()
#         if self.is_valid():
#             servico = self.cleaned_data['servico']
#             if servico:
#                 q = q & Q(servico__nome__icontains=servico)
#             titulo = self.cleaned_data['titulo']
#             if titulo:
#                 q = q & Q(titulo__icontains=titulo)
#             descricao = self.cleaned_data['descricao']
#             if descricao:
#                 q = q & Q(descricao__icontains=descricao)

#             data_ini = self.cleaned_data['data_ini']
#             if data_ini:
#                 q = q & Q(data__gte=data_ini)
#             data_fim = self.cleaned_data['data_fim']
#             if data_fim:
#                 q = q & Q(data__lte=data_fim)
#             confirmado = self.cleaned_data['confirmado']
#             if confirmado:
#                 q = q & Q(confirmado=True)
#             pago = self.cleaned_data['pago']
#             if pago:
#                 q = q & Q(pago=True)

#         return Tarefa.objects.filter(q)
#         return Tarefa.objects.all()
