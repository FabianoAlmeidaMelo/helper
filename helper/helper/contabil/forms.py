from django import forms
from helper.core.forms import BaseSearchForm
from django.db.models import Q
from django.views.generic.list import ListView
from helper.core.models import User

class ClienteUserSearchForm(forms.Form):
    '''
    Busca Users clientes do Contador 
    '''
    nome = forms.CharField(label=u'Nome', required=False)
    email = forms.CharField(label=u'email', required=False)
    

    def __init__(self, *args, **kargs):
        self.conta = kargs.pop('conta', None) # conta do contador
        super(ClienteUserSearchForm, self).__init__(*args, **kargs)
        self.contas_ids = self.conta.contador.conta_core.filter(tipo=2).values_list('id', flat=True)

    def get_queryset(self):
        q = Q(conta__in=self.contas_ids)
        if self.is_valid():
            email = self.cleaned_data['email']
            if email:
                q = q & Q(email__icontains=email)
            nome = self.cleaned_data['nome']
            if nome:
                q = q & Q(nome__icontains=nome)
        return User.objects.filter(q)