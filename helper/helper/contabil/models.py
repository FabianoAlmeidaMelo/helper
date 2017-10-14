# coding: utf-8
from django.conf import settings
from django.db import models
from helper.core.models import Endereco


class Contador(models.Model):
    """
    é o perfil jurídico do cliente contador
    """
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(u'CNPJ', max_length=18)
    # Comunicação
    endereco = models.ForeignKey(Endereco, null=True, blank=True)
    telefone = models.CharField(u'Telefone', max_length=14, null=True, blank=True)
    telefone2 = models.CharField(u'Telefone 2', max_length=14, null=True, blank=True)
    celular = models.CharField(u'Celular', max_length=14, null=True, blank=True)
    email = models.EmailField(u'email', max_length=50, null=True, blank=True)
    # Contato
    nome_contato = models.CharField(u'Nome do Contato', max_length=200)
    # conta = models.ForeignKey('core.Conta')

    def __unicode__(self):
        return self.nome    

    def can_acess(self, user):
        """
        Contador em várias contas;
        os users vinculados ao Contador só tem uma Conta
        essa conta ou é tipo = 1: Contador
        ou tipo 2 : Empresarial
        """
        return user.conta in self.conta_core.filter(tipo=1)

class Setor(models.Model):
    contador = models.ForeignKey(Contador)
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome  

class SetorContato(models.Model):
    setor = models.ForeignKey(Setor)
    telefone = models.CharField(u'Telefone', max_length=14, null=True, blank=True)
    email = models.EmailField(u'email', max_length=50, null=True, blank=True)
    nome_contato = models.CharField(max_length=60)

    def __unicode__(self):
        return '%s - %s' % (self.setor.nome, self.nome_contato)  

class SetorUser(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL)
    setor = models.ForeignKey(Setor)

    def __unicode__(self):
        return '%s - %s' % (self.usuario.nome, self.setor.nome) 