# coding: utf-8
from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from helper.settings import DEFAULT_FROM_EMAIL
from helper.agenda.models import Tarefa, Conta, Agenda, Servico
from datetime import date
from django.db.models import Q


class Command(BaseCommand):

    def handle(self, *args, **options):
        '''
        ref #30:
        comando:
        python manage.py send_mail_diario_tarefas
        '''
        hoje = date(2017,8,13)
        hoje = date.today()
        tarefas = Tarefa.objects.filter(Q(pago=False)|Q(pago=None), data_ini=hoje)
        servico_ids = list(set(tarefas.values_list('servico_id', flat=True)))
        agenda_ids = list(set(Servico.objects.filter(id__in=servico_ids).values_list('agenda_id', flat=True)))
        contas_ids = list(set(Agenda.objects.filter(id__in=agenda_ids).values_list('conta_id', flat=True)))
        contas = Conta.objects.filter(id__in=contas_ids)
        if tarefas.count():
            for conta in contas:
                self.send_mail_alerta_tarefa_diario(conta, hoje)

    def send_mail_alerta_tarefa_diario(self, conta, hoje):

        msg = u'Control H alerta para suas tarefas de hoje:\n'
        tarefas_alerta = Tarefa.objects.filter(Q(pago=False)|Q(pago=None), servico__agenda__conta=conta, data_ini=hoje).order_by('servico__agenda')
        for tarefa in tarefas_alerta:
            tipo = tarefa.get_tipo_display() or u''
            msg += u'\n%s ; %s; valor: %s R$ %s \n ' % (tarefa.servico.agenda.nome, tarefa.servico.nome, tipo, str(tarefa.valor))
            msg += 80 * u'-'

        send_mail(u'Alerta diário', msg, DEFAULT_FROM_EMAIL, [conta.dono.email], fail_silently=False)



    def envia_email_retratacao_tcra(self, emails):
        '''
        '''
        if emails:
            emails.append(u'fabiano@znc.com.br')
            emails.append(u'financeiro.programas@sosma.org.br ')

            mensagem = u'Caros requerentes do Programa Florestas do Futuro TCRA,\n\n'
            mensagem += u'Comunicamos que em virtude de atualizações e aprimoramentos do sistema de gestão da Fundação SOS Mata Atlântica, o sistema realizou o envio de e-mails, com as instruções sobre o primeiro acesso à plataforma..\n\n'
            mensagem += u'Favor desconsiderar as mensagens anteriores, pois estamos trabalhando para a geração de novos acessos à plataforma de gestão.:\n\n'
            mensagem += u'Em breve, cada responsável será notificado com os dados de login e senha para o site.\n\n'
            mensagem += u'Pedimos desculpas pelo transtorno e seguimos à disposição.\n\n'
            mensagem += u'Cordialmente.\n\n'
            mensagem += assinatura_email_geral()

        #     send_mail(
        #         u'AJUSTE SISTEMA',
        #         mensagem,
        #         DEFAULT_FROM_EMAIL,
        #         emails,
        #         fail_silently=False
        # )

            email = EmailMessage(u'AJUSTE SISTEMA',
                                 mensagem, DEFAULT_FROM_EMAIL,
                                 [], emails, headers={'Reply-To': DEFAULT_FROM_EMAIL})
            email.send(fail_silently=False)

