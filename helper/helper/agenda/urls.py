# coding: utf-8
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    '',
    #  agenda
    url(
        r'^agenda_list/$',
        'helper.agenda.views.agenda_list', name='agenda_list'
        ),
    url(
        r'^agenda_form/$',
        'helper.agenda.views.agenda_form', name='agenda_add'
        ),
    url(
        r'^agenda_form/(?P<pk>\d+)/$',
        'helper.agenda.views.agenda_form', name='agenda_edit'
        ),
    #  serviço
    url(
        r'^servico_list/$',
        'helper.agenda.views.servico_list', name='servico_list'
        ),
    url(
        r'^servico_form/$',
        'helper.agenda.views.servico_form', name='servico_add'
        ),
    url(
        r'^servico_form/(?P<pk>\d+)/$',
        'helper.agenda.views.servico_form', name='servico_edit'
        ),
    #  tarefa
    url(
        r'^tarefa_list/$',
        'helper.agenda.views.tarefa_list', name='tarefa_list'
        ),
    url(
        r'^tarefa_form/$',
        'helper.agenda.views.tarefa_form', name='tarefa_add'
        ),
    url(
        r'^tarefa_form/(?P<pk>\d+)/$',
        'helper.agenda.views.tarefa_form', name='tarefa_edit'
        ),
)
