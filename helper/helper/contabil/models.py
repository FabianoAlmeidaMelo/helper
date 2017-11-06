# coding: utf-8
from django.conf import settings
from django.db import models
from helper.core.models import Endereco
from helper.core.models import UserAdd, UserUpd, Conta

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


class Mensagem(UserAdd, UserUpd):
    '''
    #51
    Mensagem de Usuário Contador -> para 1 ou mais Clientes
    Mensagem Interna de Usuário Contador -> para todos os Seus Users
    mensagem de usuário cliente -> para setor do contador
    Origem é a conta do user que criou
    # do "Lado" do cliente, só users com acesso à agenda PJ podem ver as msg
    # do "Lado" do contador, só users do setor podem ver as msg, ou user com permissão p vert todas msg
    '''
    texto = models.TextField(verbose_name=u'Texto')
    setor = models.ForeignKey(Setor) # Origem ou Destino
    contas = models.ManyToManyField(Conta, through='ContaMensagem') # 1 msg pode ir para 1 ou 'n' contas
    # filename = models.FileField(u'Anexo', upload_to=file_anexo_msg_contrato, max_length=300, null=True, blank=True)

    class Meta:
        ordering = ('-date_add',)

    def __unicode__(self):
        return 'MSG de :%s ; em: %s' % (self.user_add.nome, self.date_add.date()) 

    def can_edit(self, user):
        '''
        Se ainda não foi 'lida'
        pode editar
        '''
        if not self.pk:
            return True
        return all([self.contamensagem_set.filter(user__isnull=False).count() < 1,
                    self.user_add.conta == user.conta])


class ContaMensagem(models.Model):
    '''
    #51
    registra:
        as contas destinatárias das Mensagens
        a data hora que o destinatário abriu a mensagem
    '''
    mensagem = models.ForeignKey(Mensagem)
    conta = models.ForeignKey(Conta)
    # data que o destinatário 'Leu':
    data = models.DateTimeField(null=True, blank=True)
    # user que 'Leu': abriu a msg:
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True)