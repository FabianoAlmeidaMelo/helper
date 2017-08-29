# coding: utf-8
from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from helper.settings import DEFAULT_FROM_EMAIL
from helper.agenda.models import Tarefa, Conta, Agenda, Servico
from datetime import date
from django.db.models import Q

"""ref #30
cat /etc/cron.d/helper

sudo nano /etc/cron.d/helper
05 01 * * * ubuntu /var/www/projetos/helper/helper/helper/scripts/send_mail_diario_tarefas.sh 2>&1 > /tmp/email_tarefas_py.txt

# torna o arquivo executável:
chmod +x /var/www/projetos/helper/helper/helper/scripts/send_mail_diario_tarefas.sh 

sudo systemctl status cron
sudo systemctl restart cron
"""

class Command(BaseCommand):

    def handle(self, *args, **options):
        '''
        ref #30:
        comando:
        python manage.py send_mail_diario_tarefas
        # hoje = date(2017,8,8)
        '''
        hoje = date.today()
        tarefas = Tarefa.objects.filter(Q(pago=False)|Q(pago=None), data_ini=hoje)
        servico_ids = list(set(tarefas.values_list('servico_id', flat=True)))
        agenda_ids = list(set(Servico.objects.filter(id__in=servico_ids).values_list('agenda_id', flat=True)))
        contas_ids = list(set(Agenda.objects.filter(id__in=agenda_ids).values_list('conta_id', flat=True)))
        contas = Conta.objects.filter(id__in=contas_ids)
        if tarefas.count():
            for conta in contas:
                self.send_mail_alerta_tarefa_diario(conta, hoje)
        print u'Envio de emails de Tarefas do dia:', hoje
        print u'Nr de Contas apitas:', contas.count(), 

    def send_mail_alerta_tarefa_diario(self, conta, hoje):

        msg = u'Control H alerta para suas tarefas de hoje:\n'
        tarefas_alerta = Tarefa.objects.filter(Q(pago=False)|Q(pago=None), servico__agenda__conta=conta, data_ini=hoje).order_by('servico__agenda')
        for tarefa in tarefas_alerta:
            tipo = tarefa.get_tipo_display() or u''
            msg += u'\n%s ; %s; %s, Valor: %s R$ %s \n ' % (tarefa.servico.agenda.nome, tarefa.servico.nome, tipo, tareafa.titulo, str(tarefa.valor))
            msg += 80 * u'-'

        send_mail(u'Alerta diário', msg, DEFAULT_FROM_EMAIL, [conta.dono.email], fail_silently=False)
