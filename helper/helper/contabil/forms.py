# coding: utf-8
from django import forms
from helper.core.forms import BaseSearchForm
from django.db.models import Q
from django.views.generic.list import ListView
from helper.core.models import User
from helper.contabil.models import (
    Contador,
    Setor,
)

class ContadorUserForm(forms.ModelForm):
    """ClienteUserForm
    Formulário de cadastro e edição
    de usuários do Contador (sócios e funcionarios do escritório)
    """

    def __init__(self, *args, **kargs):
        self.conta = kargs.pop('conta', None)
        super(ContadorUserForm, self).__init__(*args, **kargs)
        if not self.instance.pk:
            self.fields['is_active'].widget = forms.HiddenInput()

    class Meta:
        model = User
        fields = ( 'email',
                   'nome',
                   'nascimento',
                   'profissao',
                   'sexo',
                   'is_active')

    def save(self, *args, **kargs):
        self.instance.conta = self.conta
        instance = super(ContadorUserForm, self).save(*args, **kargs)

        return instance


class ClienteUserForm(forms.ModelForm):
    """
    Formulário de cadastro e edição
    de usuários Clientes do Contador
    """

    def __init__(self, *args, **kargs):
        self.contador = kargs.pop('contador', None)
        super(ClienteUserForm, self).__init__(*args, **kargs)

    class Meta:
        model = User
        fields = ( 'email', # TODO: enviar email com a senha; depois do 1º acesso, email, deixa de ser editável
                   'nome',
                   'nascimento',
                   'profissao',
                   'sexo')

    def save(self, *args, **kargs):
        # TODO:
        # se user Novo, criar a Conta, conta.tipo = 2
        # self.instance.conta = self.conta
        instance = super(ClienteUserForm, self).save(*args, **kargs)
        created = instance.set_conta(self.contador)
        if created:
            print "\n: CRIADO - TODO: send mail com a senha provisória"
        else:
            print "\nNÂO CRIADO"

        return instance


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
        model = Setor
        fields = ('nome',)

    def save(self, *args, **kargs):
        self.instance.contador = self.contador
        instance = super(SetorForm, self).save(*args, **kargs)
        instance.save()
        return instance


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


class ContadorUserSearchForm(forms.Form):
    '''
    Busca Users do Contador 
    '''
    nome = forms.CharField(label=u'Nome', required=False)
    email = forms.CharField(label=u'email', required=False)
    

    def __init__(self, *args, **kargs):
        self.conta = kargs.pop('conta', None) # conta do contador
        super(ContadorUserSearchForm, self).__init__(*args, **kargs)
        self.contas_ids = self.conta.contador.conta_core.filter(tipo=1).values_list('id', flat=True)

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