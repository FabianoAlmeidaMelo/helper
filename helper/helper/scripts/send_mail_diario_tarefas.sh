#!/bin/bash
source /home/ubuntu/.virtualenvs/helper/bin/activate
PYTHONIOENCODING=utf_8 /var/www/projetos/helper/helper/manage.py send_mail_diario_tarefas $1