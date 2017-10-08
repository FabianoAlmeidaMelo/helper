# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from helper.agenda.models import Conta as ContaAgenda, Agenda 
from helper.core.models import Conta as ContaCore


class Command(BaseCommand):
    '''
    #42
    python manage.py seta_conta_com_conta_core
    '''
    def handle(self, *args, **options):
        for conta_core in ContaCore.objects.all():  # depois da 0007
            self.setar_conta_core_na_agenda(conta_core)

    def setar_conta_core_na_agenda(self, conta_core):
        agendas = Agenda.objects.filter(conta_core=conta_core)
        for agenda in agendas:  # uma conta pode ter varias agendas
            agenda.conta = conta_core
            agenda.save()