# coding: utf-8

from django import forms
from django.db.models import Q
from .models import (
    Agenda,
    Tarefa,
)

from bootstrap_toolkit.widgets import BootstrapDateInput


class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = (
                    'nome',
                    'observacao',
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
    titular = forms.CharField(label=u'Titular', required=False)
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
    confirmado = forms.BooleanField(label='confirmado', required=False)
    pago = forms.BooleanField(label='confirmada', required=False)

    def get_queryset(self):
        q = Q()
        if self.is_valid():
            titular = self.cleaned_data['titular']
            if titular:
                q = q & Q(titular__nome__icontains=titular)
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

            return Tarefa
        return []
