from django import forms
from helper.core.forms import BaseSearchForm
from django.db.models import Q
from django.views.generic.list import ListView
from helper.core.models import User

class ClienteUserSearchForm(BaseSearchForm):
    '''
    Busca Users clientes do Contador 
    '''
    nome = forms.CharField(label=u'Nome', required=False)
    user = forms.ModelChoiceField(label=u'Selecione a Agenda', queryset=User.objects.all(), required=False)
    

    def __init__(self, *args, **kargs):
        self.conta = kargs.pop('conta', None) # conta do contador
        super(ClienteUserSearchForm, self).__init__(*args, **kargs)
        self.contas_ids = self.conta.contador.conta_core.filter(tipo=2).values_list('id', flat=True)
        self.fields['user'].queryset = User.objects.filter(conta__in=self.contas_ids)

    def get_queryset(self):
        q = Q(conta__in=self.contas_ids)
        if self.is_valid():
            # user = self.cleaned_data['user']
            # if user:
            #     q = q & Q(agenda=agenda)
            nome = self.cleaned_data['nome']
            if nome:
                q = q & Q(nome__icontains=nome)
        return User.objects.filter(q)