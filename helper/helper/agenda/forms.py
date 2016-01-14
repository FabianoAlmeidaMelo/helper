# coding: utf-8

from django import forms
from django.db.models import Q
from .models import (
    Agenda,
    Servico,
    Tarefa,
)

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
                    )


class TarefaSearchForm(forms.Form):
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

    def get_queryset(self):
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
                q = q & Q(data__gte=data_ini)
            data_fim = self.cleaned_data['data_fim']
            if data_fim:
                q = q & Q(data__lte=data_fim)
            confirmado = self.cleaned_data['confirmado']
            if confirmado:
                q = q & Q(confirmado=True)
            pago = self.cleaned_data['pago']
            if pago:
                q = q & Q(pago=True)

            return Tarefa.objects.filter(q)

        return Tarefa.objects.filter(q)
        # return Tarefa.objects.all()
