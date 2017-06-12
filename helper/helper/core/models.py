# coding: utf-8

from django.db import models
from django.utils import timezone

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
)

SEXO = (
    (1, "M"),
    (2, "F"),
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


class User(AbstractBaseUser):
    '''
        Usuário do sistema
        is_superuser == usuário Administrador
    '''
    email = models.EmailField('e-mail', unique=True)
    nome = models.CharField(verbose_name=u'Nome', max_length=100)
    is_active = models.BooleanField('ativo', default=True,)
    date_joined = models.DateTimeField(
        'data de cadastro', default=timezone.now
    )
    nascimento = models.DateField(u'Data Nascimento', null=True, blank=True)
    profissao = models.CharField(
        u'Profissão', max_length=100, null=True, blank=True
    )
    sexo = models.IntegerField(u'Sexo', choices=SEXO, null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('nome', )

    class Meta:
        verbose_name = u'Usuário'
        verbose_name_plural = u'Usuários'

    def __unicode__(self):
        return self.email
