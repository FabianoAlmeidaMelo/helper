# coding: utf-8
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)

from municipios.models import Municipio


SEXO = (
    (1, "M"),
    (2, "F"),
)


TIPO = ( # conta
    (1, u'Contador'),
    (2, u'Empresarial'),
    (3, u'Outra'),
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        now = timezone.now()
        if not email:
            raise ValueError(u'Email é obrigatório')
        email = UserManager.normalize_email(email)
        user = self.model(email=email, is_active=True, is_superuser=False,
                          last_login=now, date_joined=now, **extra_fields)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(email, password, **extra_fields)
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Conta(models.Model):
    """
    Um user só pode estar vinculado a 1 conta
    cada Conta pode ter N agendas
    as contas devem ter mais ou menos benefícios, de
    acordo com o Tipo.
    """
    dono = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='dono_conta_core')
    tipo = models.SmallIntegerField(u'tipo', choices=TIPO)
    valor = models.DecimalField(u'Valor',
                                max_digits=7,
                                decimal_places=2,
                                blank=True,
                                null=True
                            )
    validade = models.DateTimeField(u'Data')
    contador = models.ForeignKey('contabil.Contador', null=True, blank=True, related_name='conta_core')

    class Meta:
        verbose_name = u'Conta'
        verbose_name_plural = u'Contas'

    def __unicode__(self):
        return self.dono.nome

    def can_acess(self, user):
        return user in self.user_set.all()


class User(AbstractBaseUser, PermissionsMixin):
    '''
        Usuário do sistema
        is_superuser == usuário Administrador
    'email': u'',
    'first_name': u'',
    'id': None,
    'is_active': True,
    'is_staff': False,
    'is_superuser': False,
    'last_login': None,
    'last_name': u'',
    'password': u'',
    'username': u''
    '''
    email = models.EmailField('e-mail', unique=True)
    nome = models.CharField(verbose_name=u'Nome', max_length=100)
    is_active = models.BooleanField('ativo', default=True)

    is_staff = models.BooleanField('ativo', default=False)
    date_joined = models.DateTimeField(
        'data de cadastro', default=timezone.now
    )
    nascimento = models.DateField(u'Data Nascimento', null=True, blank=True)
    profissao = models.CharField(
        u'Profissão', max_length=100, null=True, blank=True
    )
    sexo = models.IntegerField(u'Sexo', choices=SEXO, null=True, blank=True)
    conta = models.ForeignKey(Conta, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('nome', )

    class Meta:
        verbose_name = u'Usuário'
        verbose_name_plural = u'Usuários'

    def __unicode__(self):
        return self.email

    def get_short_name(self):
        return self.nome

    def get_group_name(self):
        group = self.groups.all().last()
        if group:
            return group.name
        return 'Cliente'

class Endereco(models.Model):
    '''
    #26
    '''
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(verbose_name=u'Número', max_length=50)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    bairro = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio)

    def __unicode__(self):
        return u"%s - %s" % (self.cep, self.numero)

    class Meta:
        verbose_name = u'Endereço'

