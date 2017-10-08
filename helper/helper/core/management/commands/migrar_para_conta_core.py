# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from helper.agenda.models import Conta as ContaAgenda, Agenda 
from helper.core.models import Conta as ContaCore


class Command(BaseCommand):
    '''
    #42
    python manage.py migrar_para_conta_core
    '''
    def handle(self, *args, **options):
        contas_agenda = ContaAgenda.objects.all()
        for conta in contas_agenda:  # depois da 0006
            self.popula_core(conta)
        # for conta_core in ContaCore.objects.all():  # depois da 0007
        #     self.setar_conta_core_na_agenda(conta_core)


    def popula_core(self, conta):
        try:
            conta_core, create = ContaCore.objects.get_or_create(
                id= conta.id,
                tipo=conta.tipo,
                dono=conta.dono,
                valor=conta.valor,
                validade=conta.validade,
                contador=conta.contador)
            if create:
                print conta_core.id, u'Criada'
            else:
                print conta_core.id, u'Editada'
        except Exception as e:
            raise CommandError("Error: {}".format(e))

    # def setar_conta_core_na_agenda(self, conta_core):
    #     agendas = Agenda.objects.filter(conta__id=conta_core.id)
    #     for agenda in agendas:  # uma conta pode ter varias agendas
    #         agenda.conta_core = conta_core
    #         agenda.save()


        
        