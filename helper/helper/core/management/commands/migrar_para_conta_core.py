# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from helper.agenda.models import Conta as ContaAgenda 
from helper.core.models import Conta as ContaCore


class Command(BaseCommand):
    '''
    #42
    python manage.py migrar_para_conta_core
    '''
    def handle(self, *args, **options):
        try:
            self.popula_core()
        except Exception as e:
            raise CommandError("An error has occurred: {}".format(e))

        self.popula_core()

    def popula_core(self):
        contas_agenda = ContaAgenda.objects.all()
        for conta in contas_agenda:
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



        
        