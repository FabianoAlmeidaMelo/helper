# coding: utf-8
from django.conf.urls import patterns
from django.conf.urls import url

urlpatterns = patterns(
    '',
    #  agenda
    url(
        r'^agenda_list/conta/(?P<conta_pk>\d+)/$',
        'helper.agenda.views.agenda_list', name='agenda_list'
        ),
    url(
        r'^agenda_form/conta/(?P<conta_pk>\d+)/$',
        'helper.agenda.views.agenda_form', name='agenda_add'
        ),
    url(
        r'^agenda_form/conta/(?P<conta_pk>\d+)/(?P<pk>\d+)/$',
        'helper.agenda.views.agenda_form', name='agenda_edit'
        ),
    #  serviço
    url(
        r'^servico_list/conta/(?P<conta_pk>\d+)/$',
        'helper.agenda.views.servico_list', name='servico_list'
        ),
    url(
        r'^servico_form/conta/(?P<conta_pk>\d+)/$',
        'helper.agenda.views.servico_form', name='servico_add'
        ),
    url(
        r'^servico_form/conta/(?P<conta_pk>\d+)/(?P<pk>\d+)/$',
        'helper.agenda.views.servico_form', name='servico_edit'
        ),
    #  TAREFAS
    url(
        r'^tarefa_list/conta/(?P<conta_pk>\d+)$',
        'helper.agenda.views.tarefa_list', name='tarefa_list'
        ),
    url(
        r'^agenda_tarefa_list/conta/(?P<conta_pk>\d+)/agenda/(?P<agenda_pk>\d+)$',
        'helper.agenda.views.agenda_tarefa_list', name='agenda_tarefa_list'
        ),

    # url(r'^agenda_tarefa_list/conta/(?P<conta_pk>\d+)/set_status/(?P<tarefa_pk>\d+)/$',
    #     'helper.agenda.views.set_tarefa_status', name="set_tarefa_status"
    #     ),
    url(r'^agenda_tarefa_list/set_status/(?P<tarefa_pk>\d+)/$',
        'helper.agenda.views.set_tarefa_status', name="set_tarefa_status"
        ),
    url(
        r'^agenda_tarefa_form/conta/(?P<conta_pk>\d+)/(?P<agenda_pk>\d+)$',
        'helper.agenda.views.tarefa_form', name='agenda_tarefa_add'
        ),
    url(
        r'^tarefa_form/conta/(?P<conta_pk>\d+)/$',
        'helper.agenda.views.tarefa_form', name='tarefa_add'
        ),
    url(
        r'^tarefa_form/conta/(?P<conta_pk>\d+)/(?P<pk>\d+)/$',
        'helper.agenda.views.tarefa_form', name='tarefa_edit'
        ),
    url(
        r'^agenda_tarefa_form/conta/(?P<conta_pk>\d+)/(?P<agenda_pk>\d+)/(?P<pk>\d+)/$',
        'helper.agenda.views.tarefa_form', name='agenda_tarefa_edit'
        ),


    #  Cartão Credito
    url(
        r'^cartao_list/conta/(?P<conta_pk>\d+)/$',
        'helper.agenda.views.cartao_list', name='cartao_list'
        ),
    url(
        r'^cartao_form/conta/(?P<conta_pk>\d+)/$',
        'helper.agenda.views.cartao_form', name='cartao_add'
        ),
    url(
        r'^cartao_form/conta/(?P<conta_pk>\d+)/(?P<pk>\d+)/$',
        'helper.agenda.views.cartao_form', name='cartao_edit'
        ),
)
