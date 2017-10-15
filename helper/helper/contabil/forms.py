from django import forms
from helper.core.forms import BaseSearchForm
from django.db.models import Q
from django.views.generic.list import ListView
from helper.core.models import User
from helper.contabil.models import (
	Contador,
	Setor,
)


class ContadorForm(forms.ModelForm):

    def __init__(self, *args, **kargs):
        self.conta = kargs.pop('conta', None)
        super(ContadorForm, self).__init__(*args, **kargs)

    class Meta:
        model = Contador
        fields = ('nome',
                  'endereco',
                  'telefone',
                  'telefone2',
                  'celular',
                  'email',
                  'nome_contato')

class SetorForm(forms.ModelForm):

    def __init__(self, *args, **kargs):
        self.contador = kargs.pop('contador', None)
        super(SetorForm, self).__init__(*args, **kargs)

    class Meta:
        model = Contador
        fields = ('nome',)

    def save(self):
        self.instance.contador = self.contador
        self.instance.save()


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


class SetorListSearchForm(forms.Form):
    '''
    Busca Setores do Contador 
    '''
    nome = forms.CharField(label=u'Nome', required=False)
    
    def __init__(self, *args, **kargs):
        self.contador = kargs.pop('contador', None)
        super(SetorListSearchForm, self).__init__(*args, **kargs)

    def get_queryset(self):
        q = Q(contador=self.contador)
        if self.is_valid():
            nome = self.cleaned_data['nome']
            if nome:
                q = q & Q(nome__icontains=nome)
        return Setor.objects.filter(q)