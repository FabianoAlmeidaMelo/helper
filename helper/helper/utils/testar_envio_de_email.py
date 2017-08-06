# -*- coding: utf-8 -*-
from django.core.mail import send_mail
from datetime import datetime
from helper.settings import DEFAULT_FROM_EMAIL


def send_mail_teste():
    '''
    ref #29
    testa envio de emails
    Ex: from helper.utils.testar_envio_de_email import *
    '''

    emails = [u'falmeidamelo@uol.com.br']

    mensagem = u'Teste de envio de emails do control H - %s' % datetime.today()

    if emails:
        send_mail(
            u'Teste de envio/ Control H',
            mensagem,
            DEFAULT_FROM_EMAIL,
            emails,
            fail_silently=False,
        )
